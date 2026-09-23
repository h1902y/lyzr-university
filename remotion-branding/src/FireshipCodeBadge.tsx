import React from "react";
import {
  AbsoluteFill,
  Img,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
  staticFile,
} from "remotion";

export interface FireshipBadgeProps {
  title?: string;
  codeSnippet?: string;
  lessonNum?: string;
}

export const FireshipCodeBadge: React.FC<FireshipBadgeProps> = ({
  title = "Swapping LLM Providers & Structured Outputs",
  codeSnippet = "agent = studio.create_agent(provider='gpt-4o')",
  lessonNum = "03",
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const popSpring = spring({
    frame,
    fps,
    config: { damping: 10, stiffness: 220, mass: 0.5 },
  });

  const exitOpacity = interpolate(frame, [100, 120], [1, 0], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill
      style={{
        pointerEvents: "none",
        display: "flex",
        flexDirection: "column",
        justifyContent: "flex-end",
        alignItems: "flex-start",
        padding: "60px 80px",
        boxSizing: "border-box",
        opacity: exitOpacity,
      }}
    >
      {/* High-Speed Tech Pill Badge (Fireship Style) */}
      <div
        style={{
          transform: `scale(${interpolate(popSpring, [0, 1], [0.8, 1])})`,
          opacity: interpolate(popSpring, [0, 1], [0, 1]),
          backgroundColor: "#0D1117",
          border: "2px solid #38BDF8",
          borderRadius: "16px",
          padding: "20px 32px",
          boxShadow: "0 15px 35px rgba(0, 0, 0, 0.8), 0 0 25px rgba(56, 189, 248, 0.3)",
          display: "flex",
          flexDirection: "column",
          gap: "10px",
          maxWidth: "1000px",
        }}
      >
        <div style={{ display: "flex", alignItems: "center", gap: "14px" }}>
          <Img src={staticFile("lyzr-official-logo-white.svg")} style={{ height: "24px" }} />
          <span style={{ color: "#38BDF8", fontSize: "13px", fontWeight: 800, letterSpacing: "2px" }}>
            LESSON {lessonNum} · CODE QUICKSTART
          </span>
        </div>

        <div style={{ color: "#FFFFFF", fontSize: "32px", fontWeight: 800, fontFamily: "'Inter', sans-serif" }}>
          {title}
        </div>

        {codeSnippet && (
          <div
            style={{
              backgroundColor: "#161B22",
              color: "#7EE787",
              fontFamily: "'SF Mono', Monaco, Menlo, monospace",
              fontSize: "18px",
              padding: "10px 16px",
              borderRadius: "8px",
              borderLeft: "4px solid #7EE787",
            }}
          >
            <code>{codeSnippet}</code>
          </div>
        )}
      </div>
    </AbsoluteFill>
  );
};
