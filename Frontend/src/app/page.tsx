import Link from "next/link";
import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import FloatingBackground from "@/components/FloatingBackground";
import ScrollAnimations from "@/components/ScrollAnimations";
import HeroVisual from "@/components/HeroVisual";

const features = [
  {
    title: "Workflow Studio",
    desc: "Build visually or just describe what you need. Drag-and-drop a directed graph on the canvas, or type a plain-English prompt and let AI scaffold the entire flow. Validate, version-compare, and refine — your way.",
    color: "#4f46e5",
    bg: "rgba(79,70,229,0.08)",
    icon: (
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="w-6 h-6"><path strokeLinecap="round" strokeLinejoin="round" d="M9.594 3.94c.09-.542.56-.94 1.11-.94h2.593c.55 0 1.02.398 1.11.94l.213 1.281c.063.374.313.686.645.87.074.04.147.083.22.127.325.196.72.257 1.075.124l1.217-.456a1.125 1.125 0 0 1 1.37.49l1.296 2.247a1.125 1.125 0 0 1-.26 1.431l-1.003.827c-.293.241-.438.613-.43.992a7.723 7.723 0 0 1 0 .255c-.008.378.137.75.43.991l1.004.827c.424.35.534.955.26 1.43l-1.298 2.247a1.125 1.125 0 0 1-1.369.491l-1.217-.456c-.355-.133-.75-.072-1.076.124a6.47 6.47 0 0 1-.22.128c-.331.183-.581.495-.644.869l-.213 1.281c-.09.543-.56.94-1.11.94h-2.594c-.55 0-1.019-.398-1.11-.94l-.213-1.281c-.062-.374-.312-.686-.644-.87a6.52 6.52 0 0 1-.22-.127c-.325-.196-.72-.257-1.076-.124l-1.217.456a1.125 1.125 0 0 1-1.369-.49l-1.297-2.247a1.125 1.125 0 0 1 .26-1.431l1.004-.827c.292-.24.437-.613.43-.991a6.932 6.932 0 0 1 0-.255c.007-.38-.138-.751-.43-.992l-1.004-.827a1.125 1.125 0 0 1-.26-1.43l1.297-2.247a1.125 1.125 0 0 1 1.37-.491l1.216.456c.356.133.751.072 1.076-.124.072-.044.146-.086.22-.128.332-.183.582-.495.644-.869l.214-1.28Z" /><path strokeLinecap="round" strokeLinejoin="round" d="M15 12a3 3 0 1 1-6 0 3 3 0 0 1 6 0Z" /></svg>
    ),
  },
  {
    title: "Workspaces & Governance",
    desc: "Give every department its own workspace with tailored tools, dashboards, and delegated admin. Run cross-workspace workflows while enforcing hierarchical access controls org-wide.",
    color: "#06b6d4",
    bg: "rgba(6,182,212,0.08)",
    icon: (
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="w-6 h-6"><path strokeLinecap="round" strokeLinejoin="round" d="M3.75 21h16.5M4.5 3h15M5.25 3v18m13.5-18v18M9 6.75h1.5m-1.5 3h1.5m-1.5 3h1.5m3-6H15m-1.5 3H15m-1.5 3H15M9 21v-3.375c0-.621.504-1.125 1.125-1.125h3.75c.621 0 1.125.504 1.125 1.125V21" /></svg>
    ),
  },
  {
    title: "Process Intelligence",
    desc: "Live dashboards meet AI-driven insights. Automatically spot bottlenecks, predict SLA breaches before they happen, flag anomalous patterns, and surface actionable optimisation recommendations.",
    color: "#8b5cf6",
    bg: "rgba(139,92,246,0.08)",
    icon: (
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="w-6 h-6"><path strokeLinecap="round" strokeLinejoin="round" d="M3.75 3v11.25A2.25 2.25 0 0 0 6 16.5h2.25M3.75 3h-1.5m1.5 0h16.5m0 0h1.5m-1.5 0v11.25A2.25 2.25 0 0 1 18 16.5h-2.25m-7.5 0h7.5m-7.5 0-1 3m8.5-3 1 3m0 0 .5 1.5m-.5-1.5h-9.5m0 0-.5 1.5M9 11.25v1.5M12 9v3.75m3-6v6" /></svg>
    ),
  },
  {
    title: "Adaptive Routing",
    desc: "The platform learns how your team works — who approves fastest, who's overloaded, who's idle. Tasks get routed intelligently so work flows through people, not around them.",
    color: "#f59e0b",
    bg: "rgba(245,158,11,0.08)",
    icon: (
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="w-6 h-6"><path strokeLinecap="round" strokeLinejoin="round" d="M15 19.128a9.38 9.38 0 0 0 2.625.372 9.337 9.337 0 0 0 4.121-.952 4.125 4.125 0 0 0-7.533-2.493M15 19.128v-.003c0-1.113-.285-2.16-.786-3.07M15 19.128v.106A12.318 12.318 0 0 1 8.624 21c-2.331 0-4.512-.645-6.374-1.766l-.001-.109a6.375 6.375 0 0 1 11.964-3.07M12 6.375a3.375 3.375 0 1 1-6.75 0 3.375 3.375 0 0 1 6.75 0Zm8.25 2.25a2.625 2.625 0 1 1-5.25 0 2.625 2.625 0 0 1 5.25 0Z" /></svg>
    ),
  },
  {
    title: "Simulation Engine",
    desc: "Test every workflow in a digital twin before it touches production. Throw synthetic workloads at it, see where delays pile up, and know if your SLAs will hold — all risk-free.",
    color: "#ec4899",
    bg: "rgba(236,72,153,0.08)",
    icon: (
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="w-6 h-6"><path strokeLinecap="round" strokeLinejoin="round" d="M9.75 3.104v5.714a2.25 2.25 0 0 1-.659 1.591L5 14.5M9.75 3.104c-.251.023-.501.05-.75.082m.75-.082a24.301 24.301 0 0 1 4.5 0m0 0v5.714c0 .597.237 1.17.659 1.591L19.8 15.3M14.25 3.104c.251.023.501.05.75.082M19.8 15.3l-1.57.393A9.065 9.065 0 0 1 12 15a9.065 9.065 0 0 0-6.23.693L5 14.5m14.8.8 1.402 1.402c1.232 1.232.65 3.318-1.067 3.611A48.309 48.309 0 0 1 12 21c-2.773 0-5.491-.235-8.135-.687-1.718-.293-2.3-2.379-1.067-3.61L5 14.5" /></svg>
    ),
  },
  {
    title: "Open Integration Layer",
    desc: "Webhooks in, REST APIs out, script nodes in between, and a library of pluggable connectors. Wire FlowEngine into your existing stack in minutes, not sprints.",
    color: "#22c55e",
    bg: "rgba(34,197,94,0.08)",
    icon: (
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="1.5" stroke="currentColor" className="w-6 h-6"><path strokeLinecap="round" strokeLinejoin="round" d="M13.19 8.688a4.5 4.5 0 0 1 1.242 7.244l-4.5 4.5a4.5 4.5 0 0 1-6.364-6.364l1.757-1.757m13.35-.622 1.757-1.757a4.5 4.5 0 0 0-6.364-6.364l-4.5 4.5a4.5 4.5 0 0 0 1.242 7.244" /></svg>
    ),
  },
];

const steps = [
  { num: "1", title: "Create Your Organisation", desc: "Sign up, name your org, and invite your team. FlowEngine sets up your workspace — ready to go in under a minute." },
  { num: "2", title: "Design Workflows", desc: "Use the visual builder to map out your processes. Add triggers, conditions, and actions with a simple drag-and-drop interface." },
  { num: "3", title: "Automate & Scale", desc: "Deploy workflows across teams and departments. Monitor in real-time and let the platform handle the rest while you focus on growth." },
];

const testimonials = [
  { text: "“Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam quis nostrud.”", name: "A. Lorem", role: "Operations Director, Acme Corp", initials: "AL", gradient: "from-indigo-500 to-cyan-500" },
  { text: "“Quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum.”", name: "B. Ipsum", role: "Technology Lead, Global Industries", initials: "BI", gradient: "from-purple-500 to-pink-500" },
  { text: "“Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum et dolorum fuga.”", name: "C. Dolor", role: "VP Operations, Enterprise Solutions Ltd", initials: "CD", gradient: "from-amber-500 to-red-500" },
];

export default function Home() {
  return (
    <>
      <FloatingBackground />
      <Navbar />
      <ScrollAnimations />

      {/* Hero */}
      <section className="pt-40 pb-24 relative z-[2] overflow-hidden">
        <div className="absolute inset-0 z-0 overflow-hidden pointer-events-none">
          <div className="absolute -top-[40%] -right-[20%] w-[700px] h-[700px] rounded-full bg-[radial-gradient(circle,rgba(79,70,229,0.08)_0%,transparent_70%)] dark:bg-[radial-gradient(circle,rgba(129,140,248,0.12)_0%,transparent_70%)]" />
          <div className="absolute -bottom-[30%] -left-[15%] w-[600px] h-[600px] rounded-full bg-[radial-gradient(circle,rgba(6,182,212,0.06)_0%,transparent_70%)] dark:bg-[radial-gradient(circle,rgba(34,211,238,0.08)_0%,transparent_70%)]" />
        </div>

        <div className="max-w-[1200px] mx-auto px-6 relative z-[1]">
          <div className="text-center max-w-[800px] mx-auto">
            <div className="inline-flex items-center gap-2 px-4 py-1.5 pl-2 bg-[var(--surface-alt)] border border-[var(--border)] rounded-full text-[0.85rem] font-medium text-[var(--text-secondary)] mb-7 animate-[fadeInDown_0.6s_ease]">
              <span className="w-2 h-2 bg-green-500 rounded-full animate-pulse" />
              Now in Public Beta &mdash; Try FlowEngine Free
            </div>
            <h1 className="text-[clamp(2.5rem,5.5vw,4rem)] font-extrabold tracking-[-0.03em] mb-6 animate-[fadeInUp_0.7s_ease]">
              Automate Your<br /><span className="gradient-text">Entire Business</span>
            </h1>
            <p className="text-[clamp(1.05rem,2vw,1.2rem)] text-[var(--text-secondary)] max-w-[600px] mx-auto mb-10 leading-[1.7] animate-[fadeInUp_0.8s_ease]">
              Build workflows, create workstations, and manage teams with an intelligent platform designed to replace complexity with clarity.
            </p>
            <div className="flex items-center justify-center gap-4 flex-wrap animate-[fadeInUp_0.9s_ease]">
              <Link href="/create-org" className="inline-flex items-center justify-center gap-2 px-8 py-4 text-base font-semibold rounded-[var(--radius-lg)] bg-[var(--primary)] text-white shadow-[0_1px_3px_rgba(79,70,229,0.3)] hover:bg-[var(--primary-dark)] hover:shadow-[0_4px_12px_rgba(79,70,229,0.35)] hover:-translate-y-[1px] transition-all">
                Create Organisation
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="2" stroke="currentColor" className="w-[18px] h-[18px]"><path strokeLinecap="round" strokeLinejoin="round" d="M13.5 4.5 21 12m0 0-7.5 7.5M21 12H3" /></svg>
              </Link>
              <Link href="/join" className="inline-flex items-center justify-center gap-2 px-8 py-4 text-base font-semibold rounded-[var(--radius-lg)] bg-[var(--surface)] text-[var(--text-primary)] border border-[var(--border)] hover:border-[var(--primary)] hover:text-[var(--primary)] hover:-translate-y-[1px] transition-all">
                <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="2" stroke="currentColor" className="w-[18px] h-[18px]"><path strokeLinecap="round" strokeLinejoin="round" d="M18 7.5v3m0 0v3m0-3h3m-3 0h-3m-2.25-4.125a3.375 3.375 0 1 1-6.75 0 3.375 3.375 0 0 1 6.75 0ZM3 19.235v-.11a6.375 6.375 0 0 1 12.75 0v.109A12.318 12.318 0 0 1 9.374 21c-2.331 0-4.512-.645-6.374-1.766Z" /></svg>
                Join Organisation
              </Link>
            </div>
          </div>

          <HeroVisual />
        </div>
      </section>

      {/* Trusted By */}
      <section className="py-16 pb-20 text-center relative z-[2] animate-on-scroll">
        <div className="max-w-[1200px] mx-auto px-6">
          <p className="text-[0.9rem] font-medium text-[var(--text-muted)] uppercase tracking-[0.1em] mb-8">Trusted by forward-thinking organisations</p>
          <div className="flex items-center justify-center gap-12 flex-wrap opacity-50">
            {["Acme Corp", "GlobalTech", "Enterprise Co", "Industry LLC", "Solutions Inc", "Dynamics Ltd"].map((name) => (
              <span key={name} className="text-[1.2rem] font-bold text-[var(--text-muted)] tracking-[0.02em]">{name}</span>
            ))}
          </div>
        </div>
      </section>

      {/* Features */}
      <section className="py-24 relative z-[2]" id="features">
        <div className="max-w-[1200px] mx-auto px-6">
          <div className="text-center max-w-[640px] mx-auto mb-16 animate-on-scroll">
            <div className="inline-flex items-center gap-1.5 text-[0.85rem] font-semibold text-[var(--primary)] uppercase tracking-[0.08em] mb-4">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="2" stroke="currentColor" className="w-4 h-4"><path strokeLinecap="round" strokeLinejoin="round" d="M9.813 15.904 9 18.75l-.813-2.846a4.5 4.5 0 0 0-3.09-3.09L2.25 12l2.846-.813a4.5 4.5 0 0 0 3.09-3.09L9 5.25l.813 2.846a4.5 4.5 0 0 0 3.09 3.09L15.75 12l-2.846.813a4.5 4.5 0 0 0-3.09 3.09Z" /></svg>
              Platform Features
            </div>
            <h2 className="text-[clamp(1.8rem,3.5vw,2.5rem)] font-extrabold tracking-[-0.02em] mb-4">Everything you need to run your business on autopilot</h2>
            <p className="text-[1.05rem] text-[var(--text-secondary)] leading-[1.7]">From drag-and-drop design to AI-generated workflows and real-time process intelligence &mdash; FlowEngine combines human creativity with machine precision.</p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {features.map((f) => (
              <div key={f.title} className="animate-on-scroll group bg-[var(--surface)] border border-[var(--border)] rounded-[var(--radius-lg)] p-8 relative overflow-hidden transition-all duration-300 hover:border-[var(--primary-light)] hover:shadow-lg hover:-translate-y-1">
                <div className="absolute top-0 left-0 right-0 h-[3px] bg-gradient-to-r from-[var(--primary)] to-[var(--accent)] opacity-0 group-hover:opacity-100 transition-opacity" />
                <div className="w-[52px] h-[52px] rounded-[14px] flex items-center justify-center mb-5 transition-transform group-hover:scale-105" style={{ background: f.bg, color: f.color }}>
                  {f.icon}
                </div>
                <h3 className="text-[1.15rem] font-bold mb-2.5">{f.title}</h3>
                <p className="text-[0.925rem] text-[var(--text-secondary)] leading-[1.65]">{f.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* How It Works */}
      <section className="py-24 bg-[rgba(248,250,252,0.8)] dark:bg-[rgba(30,41,59,0.6)] backdrop-blur-[8px] relative z-[2] transition-[background]" id="how-it-works">
        <div className="max-w-[1200px] mx-auto px-6">
          <div className="text-center max-w-[640px] mx-auto mb-16 animate-on-scroll">
            <div className="inline-flex items-center gap-1.5 text-[0.85rem] font-semibold text-[var(--primary)] uppercase tracking-[0.08em] mb-4">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="2" stroke="currentColor" className="w-4 h-4"><path strokeLinecap="round" strokeLinejoin="round" d="M3.75 13.5l10.5-11.25L12 10.5h8.25L9.75 21.75 12 13.5H3.75z" /></svg>
              How It Works
            </div>
            <h2 className="text-[clamp(1.8rem,3.5vw,2.5rem)] font-extrabold tracking-[-0.02em] mb-4">Up and running in three simple steps</h2>
            <p className="text-[1.05rem] text-[var(--text-secondary)] leading-[1.7]">Getting started with FlowEngine is fast. No complex setup, no engineering team required.</p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-3 gap-8 relative">
            <div className="hidden md:block absolute top-12 left-[16.66%] right-[16.66%] h-0.5 bg-gradient-to-r from-[var(--primary)] to-[var(--accent)] opacity-30" />
            {steps.map((s) => (
              <div key={s.num} className="text-center relative z-[1] animate-on-scroll group">
                <div className="w-16 h-16 rounded-[20px] bg-[var(--surface)] border-2 border-[var(--primary)] flex items-center justify-center text-[1.3rem] font-extrabold text-[var(--primary)] mx-auto mb-6 shadow-md transition-all group-hover:bg-[var(--primary)] group-hover:text-white group-hover:scale-[1.08]">
                  {s.num}
                </div>
                <h3 className="text-[1.2rem] font-bold mb-2.5">{s.title}</h3>
                <p className="text-[0.925rem] text-[var(--text-secondary)] leading-[1.65] max-w-[300px] mx-auto">{s.desc}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Testimonials */}
      <section className="py-24 relative z-[2]" id="testimonials">
        <div className="max-w-[1200px] mx-auto px-6">
          <div className="text-center max-w-[640px] mx-auto mb-16 animate-on-scroll">
            <div className="inline-flex items-center gap-1.5 text-[0.85rem] font-semibold text-[var(--primary)] uppercase tracking-[0.08em] mb-4">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" strokeWidth="2" stroke="currentColor" className="w-4 h-4"><path strokeLinecap="round" strokeLinejoin="round" d="M20.25 8.511c.884.284 1.5 1.128 1.5 2.097v4.286c0 1.136-.847 2.1-1.98 2.193-.34.027-.68.052-1.02.072v3.091l-3-3c-1.354 0-2.694-.055-4.02-.163a2.115 2.115 0 0 1-.825-.242m9.345-8.334a2.126 2.126 0 0 0-.476-.095 48.64 48.64 0 0 0-8.048 0c-1.131.094-1.976 1.057-1.976 2.192v4.286c0 .837.46 1.58 1.155 1.951m9.345-8.334V6.637c0-1.621-1.152-3.026-2.76-3.235A48.455 48.455 0 0 0 11.25 3c-2.115 0-4.198.137-6.24.402-1.608.209-2.76 1.614-2.76 3.235v6.226c0 1.621 1.152 3.026 2.76 3.235.577.075 1.157.14 1.74.194V21l4.155-4.155" /></svg>
              Testimonials
            </div>
            <h2 className="text-[clamp(1.8rem,3.5vw,2.5rem)] font-extrabold tracking-[-0.02em] mb-4">Loved by teams worldwide</h2>
            <p className="text-[1.05rem] text-[var(--text-secondary)] leading-[1.7]">See why thousands of organisations trust FlowEngine to streamline their operations.</p>
          </div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {testimonials.map((t) => (
              <div key={t.name} className="animate-on-scroll bg-[var(--surface)] border border-[var(--border)] rounded-[var(--radius-lg)] p-8 transition-all hover:shadow-lg hover:-translate-y-0.5">
                <div className="flex gap-0.5 mb-4">
                  {[...Array(5)].map((_, i) => (
                    <svg key={i} viewBox="0 0 20 20" className="w-[18px] h-[18px] fill-amber-400 text-amber-400"><path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z" /></svg>
                  ))}
                </div>
                <p className="text-[0.95rem] text-[var(--text-secondary)] leading-[1.7] mb-5">{t.text}</p>
                <div className="flex items-center gap-3">
                  <div className={`w-11 h-11 rounded-[12px] flex items-center justify-center font-bold text-base text-white bg-gradient-to-br ${t.gradient}`}>
                    {t.initials}
                  </div>
                  <div>
                    <div className="font-semibold text-[0.925rem]">{t.name}</div>
                    <div className="text-[0.825rem] text-[var(--text-muted)]">{t.role}</div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      <Footer />
    </>
  );
}
