"use client";

export default function HeroVisual() {
  return (
    <div className="mt-16 max-w-[900px] mx-auto animate-[fadeInUp_1s_ease]">
      <div className="relative">
        {/* Dashboard mockup */}
        <div className="bg-[var(--surface)] border border-[var(--border)] rounded-[var(--radius-xl)] shadow-[0_20px_60px_rgba(0,0,0,0.08)] dark:shadow-[0_20px_60px_rgba(0,0,0,0.3)] overflow-hidden">
          {/* Title bar */}
          <div className="flex items-center gap-2 px-4 py-3 bg-[var(--surface-alt)] border-b border-[var(--border)]">
            <div className="flex gap-1.5">
              <span className="w-3 h-3 rounded-full bg-red-400" />
              <span className="w-3 h-3 rounded-full bg-amber-400" />
              <span className="w-3 h-3 rounded-full bg-green-400" />
            </div>
            <div className="flex-1 text-center">
              <div className="inline-block px-8 py-1 bg-[var(--surface-alt)] rounded-md text-xs text-[var(--text-muted)]">flowengine.app/dashboard</div>
            </div>
          </div>

          <div className="flex min-h-[340px]">
            {/* Sidebar */}
            <div className="hidden sm:flex flex-col w-[200px] bg-[var(--surface-alt)] border-r border-[var(--border)] p-4 gap-1">
              {[
                { label: "Dashboard", active: true },
                { label: "Workflows" },
                { label: "Stations" },
                { label: "Teams" },
                { label: "Analytics" },
                { label: "Admin" },
              ].map((item) => (
                <div
                  key={item.label}
                  className={`flex items-center gap-2.5 px-3 py-2 rounded-lg text-sm font-medium transition-colors ${
                    item.active
                      ? "bg-[var(--primary)] text-white"
                      : "text-[var(--text-secondary)] hover:bg-[var(--surface-alt)]"
                  }`}
                >
                  <div className={`w-1.5 h-1.5 rounded-full ${item.active ? "bg-white" : "bg-[var(--text-muted)]"}`} />
                  {item.label}
                </div>
              ))}
            </div>

            {/* Main content */}
            <div className="flex-1 p-6">
              <div className="grid grid-cols-2 md:grid-cols-3 gap-4">
                {[
                  { label: "Active Workflows", value: "XXX", change: "+XX%", color: "text-green-500" },
                  { label: "Tasks Today", value: "X,XXX", change: "+X%", color: "text-green-500" },
                  { label: "Team Members", value: "XX", change: "+X", color: "text-blue-500" },
                  { label: "Automation Rate", value: "XX.X%", change: "+X.X%", color: "text-green-500" },
                  { label: "Avg. Completion", value: "X.Xm", change: "-XX%", color: "text-green-500" },
                  { label: "SLA Compliance", value: "XX.X%", change: "+X.X%", color: "text-green-500" },
                ].map((stat) => (
                  <div key={stat.label} className="bg-[var(--surface-alt)] rounded-[var(--radius)] p-4 border border-[var(--border)]">
                    <div className="text-xs text-[var(--text-muted)] mb-1">{stat.label}</div>
                    <div className="text-xl font-bold text-[var(--text-muted)]">{stat.value}</div>
                    <div className={`text-xs font-medium ${stat.color}`}>{stat.change}</div>
                  </div>
                ))}
              </div>

              {/* Mini chart placeholder */}
              <div className="mt-4 bg-[var(--surface-alt)] rounded-[var(--radius)] p-4 border border-[var(--border)]">
                <div className="text-xs text-[var(--text-muted)] mb-3">Weekly Throughput</div>
                <div className="flex items-end gap-1 h-16">
                  {[40, 65, 45, 80, 60, 90, 75, 95, 70, 85, 55, 92].map((h, i) => (
                    <div
                      key={i}
                      className="flex-1 bg-gradient-to-t from-indigo-500 to-cyan-400 rounded-t opacity-70 hover:opacity-100 transition-opacity"
                      style={{ height: `${h}%` }}
                    />
                  ))}
                </div>
              </div>
            </div>
          </div>
        </div>

        {/* Floating badges */}
        <div className="absolute -right-4 top-20 bg-[var(--surface)] border border-[var(--border)] rounded-[var(--radius-lg)] p-3 shadow-lg animate-[float_6s_ease-in-out_infinite] hidden lg:flex items-center gap-2">
          <div className="w-8 h-8 rounded-full bg-green-500/10 flex items-center justify-center">
            <svg className="w-4 h-4 text-green-500" fill="none" viewBox="0 0 24 24" strokeWidth="2" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" d="M4.5 12.75l6 6 9-13.5" /></svg>
          </div>
          <div>
            <div className="text-xs font-bold">Tasks Completed</div>
            <div className="text-xs text-[var(--text-muted)]">X,XXX today</div>
          </div>
        </div>

        <div className="absolute -left-4 bottom-24 bg-[var(--surface)] border border-[var(--border)] rounded-[var(--radius-lg)] p-3 shadow-lg animate-[float_6s_ease-in-out_1.5s_infinite] hidden lg:flex items-center gap-2">
          <div className="w-8 h-8 rounded-full bg-indigo-500/10 flex items-center justify-center">
            <svg className="w-4 h-4 text-indigo-500" fill="none" viewBox="0 0 24 24" strokeWidth="2" stroke="currentColor"><path strokeLinecap="round" strokeLinejoin="round" d="M3.75 13.5l10.5-11.25L12 10.5h8.25L9.75 21.75 12 13.5H3.75z" /></svg>
          </div>
          <div>
            <div className="text-xs font-bold">Automation Rate</div>
            <div className="text-xs text-[var(--text-muted)]">XX.X%</div>
          </div>
        </div>
      </div>
    </div>
  );
}
