"use client";
import { useEffect } from "react";

export default function ScrollAnimations() {
  useEffect(() => {
    // Small delay to ensure DOM is fully painted after hydration
    const timer = setTimeout(() => {
      const elements = document.querySelectorAll(".animate-on-scroll");
      const observer = new IntersectionObserver(
        (entries) => {
          entries.forEach((entry) => {
            if (entry.isIntersecting) {
              entry.target.classList.add("visible");
              observer.unobserve(entry.target);
            }
          });
        },
        { threshold: 0.1, rootMargin: "0px 0px -50px 0px" }
      );
      elements.forEach((el) => observer.observe(el));
      return () => observer.disconnect();
    }, 100);
    return () => clearTimeout(timer);
  }, []);
  return null;
}
