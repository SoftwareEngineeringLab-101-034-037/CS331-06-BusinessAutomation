"use client";

export default function AuthDecorativePanel({
  icon,
  title,
  description,
  features,
}: {
  icon: React.ReactNode;
  title: string;
  description: string;
  features: { icon: React.ReactNode; label: string; desc: string }[];
}) {
  return (
    <div className="hidden lg:flex flex-col items-center justify-center flex-1 bg-gradient-to-br from-indigo-600 via-purple-600 to-blue-600 relative overflow-hidden p-12 text-center min-h-screen">
      {/* Floating decorative circles */}
      <div className="absolute top-[-60px] right-[-40px] w-[200px] h-[200px] rounded-full bg-white/[0.06] animate-[float-slow_18s_ease-in-out_infinite]" />
      <div className="absolute bottom-[10%] left-[-30px] w-[150px] h-[150px] rounded-full bg-white/[0.04] animate-[float-slow_22s_ease-in-out_3s_infinite]" />
      <div className="absolute top-[40%] right-[15%] w-[100px] h-[100px] rounded-full bg-white/[0.05] animate-[float-slow_15s_ease-in-out_6s_infinite]" />

      <div className="relative z-[1] max-w-[360px]">
        <div className="w-[72px] h-[72px] bg-white/15 rounded-[20px] flex items-center justify-center mx-auto mb-6">
          {icon}
        </div>
        <h2 className="text-2xl font-bold text-white mb-3">{title}</h2>
        <p className="text-white/70 leading-relaxed mb-10">{description}</p>

        <div className="flex flex-col gap-4 text-left">
          {features.map((f) => (
            <div key={f.label} className="flex items-start gap-3 bg-white/[0.08] rounded-xl p-3.5 backdrop-blur-sm">
              <div className="w-9 h-9 rounded-lg bg-white/15 flex items-center justify-center shrink-0 mt-0.5">
                {f.icon}
              </div>
              <div>
                <div className="font-semibold text-white text-[0.9rem]">{f.label}</div>
                <div className="text-white/65 text-[0.8rem]">{f.desc}</div>
              </div>
            </div>
          ))}
        </div>

        <div className="mt-10">
          <div className="text-[0.75rem] text-white/50 uppercase tracking-[1px] mb-3">Trusted by teams at</div>
          <div className="flex gap-6 justify-center flex-wrap opacity-60">
            {["TechCo", "DataWorks", "CloudServ", "DevOps Ltd"].map((name) => (
              <span key={name} className="text-white font-bold text-[0.9rem]">{name}</span>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}
