"use client";
import { useEffect, useRef } from "react";
import { useTheme } from "./ThemeProvider";

const LIGHT_PALETTE = [
  { r: 79, g: 70, b: 229 },
  { r: 6, g: 182, b: 212 },
  { r: 168, g: 85, b: 247 },
  { r: 236, g: 72, b: 153 },
  { r: 34, g: 197, b: 94 },
  { r: 251, g: 191, b: 36 },
];
const DARK_PALETTE = [
  { r: 129, g: 140, b: 248 },
  { r: 34, g: 211, b: 238 },
  { r: 192, g: 132, b: 252 },
  { r: 244, g: 114, b: 182 },
  { r: 74, g: 222, b: 128 },
  { r: 253, g: 224, b: 71 },
];

const SHAPE_COUNT = 18;
const SPEED_MIN = 0.15;
const SPEED_MAX = 0.55;
const SIZE_MIN = 14;
const SIZE_MAX = 45;
const OPACITY_LIGHT = 0.38;
const OPACITY_DARK = 0.22;

interface Shape {
  x: number; y: number; size: number; kind: number;
  col: { r: number; g: number; b: number };
  opacity: number; vx: number; vy: number;
  rot: number; vr: number; pulse: number; pulseSpeed: number;
}

function rand(min: number, max: number) { return Math.random() * (max - min) + min; }

export default function FloatingBackground() {
  const canvasRef = useRef<HTMLCanvasElement>(null);
  const { theme } = useTheme();
  const shapesRef = useRef<Shape[]>([]);
  const animRef = useRef<number>(0);
  const sizeRef = useRef({ w: 0, h: 0 });

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    if (!ctx) return;

    const isDark = theme === "dark";
    const pal = isDark ? DARK_PALETTE : LIGHT_PALETTE;
    const baseOp = isDark ? OPACITY_DARK : OPACITY_LIGHT;

    function resize() {
      const dpr = window.devicePixelRatio || 1;
      const w = window.innerWidth;
      const h = window.innerHeight;
      sizeRef.current = { w, h };
      canvas!.width = w * dpr;
      canvas!.height = h * dpr;
      canvas!.style.width = w + "px";
      canvas!.style.height = h + "px";
      ctx!.setTransform(dpr, 0, 0, dpr, 0, 0);
    }

    function createShape(i: number): Shape {
      const col = pal[i % pal.length];
      const size = rand(SIZE_MIN, SIZE_MAX);
      return {
        x: rand(-50, sizeRef.current.w + 50),
        y: rand(-50, sizeRef.current.h + 50),
        size, kind: Math.floor(rand(0, 5)), col,
        opacity: rand(baseOp * 0.5, baseOp),
        vx: rand(SPEED_MIN, SPEED_MAX) * (Math.random() > 0.5 ? 1 : -1),
        vy: rand(SPEED_MIN, SPEED_MAX) * (Math.random() > 0.5 ? 1 : -1),
        rot: rand(0, Math.PI * 2),
        vr: rand(0.001, 0.006) * (Math.random() > 0.5 ? 1 : -1),
        pulse: rand(0, Math.PI * 2), pulseSpeed: rand(0.005, 0.015),
      };
    }

    resize();
    shapesRef.current = Array.from({ length: SHAPE_COUNT }, (_, i) => createShape(i));

    function drawCircle(s: Shape) { ctx!.beginPath(); ctx!.arc(0, 0, s.size / 2, 0, Math.PI * 2); ctx!.fill(); }
    function drawRoundedRect(s: Shape) {
      const h2 = s.size / 2, r = s.size * 0.25;
      ctx!.beginPath();
      ctx!.moveTo(-h2 + r, -h2); ctx!.lineTo(h2 - r, -h2);
      ctx!.quadraticCurveTo(h2, -h2, h2, -h2 + r); ctx!.lineTo(h2, h2 - r);
      ctx!.quadraticCurveTo(h2, h2, h2 - r, h2); ctx!.lineTo(-h2 + r, h2);
      ctx!.quadraticCurveTo(-h2, h2, -h2, h2 - r); ctx!.lineTo(-h2, -h2 + r);
      ctx!.quadraticCurveTo(-h2, -h2, -h2 + r, -h2);
      ctx!.closePath(); ctx!.fill();
    }
    function drawRing(s: Shape) {
      ctx!.beginPath(); ctx!.arc(0, 0, s.size / 2, 0, Math.PI * 2);
      ctx!.lineWidth = Math.max(1.5, s.size * 0.12); ctx!.stroke();
    }
    function drawDiamond(s: Shape) {
      const h2 = s.size / 2;
      ctx!.beginPath(); ctx!.moveTo(0, -h2); ctx!.lineTo(h2, 0);
      ctx!.lineTo(0, h2); ctx!.lineTo(-h2, 0); ctx!.closePath(); ctx!.fill();
    }
    function drawCross(s: Shape) {
      const arm = s.size / 2, t = Math.max(2, s.size * 0.18);
      ctx!.beginPath();
      ctx!.moveTo(-t, -arm); ctx!.lineTo(t, -arm); ctx!.lineTo(t, -t);
      ctx!.lineTo(arm, -t); ctx!.lineTo(arm, t); ctx!.lineTo(t, t);
      ctx!.lineTo(t, arm); ctx!.lineTo(-t, arm); ctx!.lineTo(-t, t);
      ctx!.lineTo(-arm, t); ctx!.lineTo(-arm, -t); ctx!.lineTo(-t, -t);
      ctx!.closePath(); ctx!.fill();
    }
    const drawFns = [drawCircle, drawRoundedRect, drawRing, drawDiamond, drawCross];

    function frame() {
      const { w, h } = sizeRef.current;
      ctx!.clearRect(0, 0, w, h);
      for (const s of shapesRef.current) {
        s.x += s.vx; s.y += s.vy; s.rot += s.vr; s.pulse += s.pulseSpeed;
        const alpha = s.opacity * (0.7 + 0.3 * Math.sin(s.pulse));
        const margin = s.size + 60;
        if (s.x < -margin) s.x = w + margin * 0.5;
        if (s.x > w + margin) s.x = -margin * 0.5;
        if (s.y < -margin) s.y = h + margin * 0.5;
        if (s.y > h + margin) s.y = -margin * 0.5;

        ctx!.save();
        ctx!.translate(s.x, s.y); ctx!.rotate(s.rot); ctx!.globalAlpha = alpha;
        const { r, g, b } = s.col;
        if (s.kind === 2) { ctx!.strokeStyle = `rgba(${r},${g},${b},1)`; }
        else { ctx!.fillStyle = `rgba(${r},${g},${b},1)`; }
        drawFns[s.kind](s);
        ctx!.restore();
      }
      animRef.current = requestAnimationFrame(frame);
    }

    frame();
    window.addEventListener("resize", resize);
    return () => {
      cancelAnimationFrame(animRef.current);
      window.removeEventListener("resize", resize);
    };
  }, [theme]);

  return <canvas ref={canvasRef} id="floatingBg" aria-hidden="true" />;
}
