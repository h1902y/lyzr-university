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

export const OutroBumper: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const logoSpring = spring({
    frame,
    fps,
    config: { damping: 15, stiffness: 140, mass: 0.6 },
  });

  const linksOpacity = interpolate(frame, [6, 18], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: "#050505",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        justifyContent: "center",
        textAlign: "center",
        boxSizing: "border-box",
        padding: "80px",
        fontFamily: "'Inter', system-ui, -apple-system, sans-serif",
      }}
    >
      {/* 1. Official Pure White Lyzr Logo Header */}
      <div
        style={{
          transform: `scale(${interpolate(logoSpring, [0, 1], [0.94, 1])})`,
          opacity: interpolate(logoSpring, [0, 1], [0, 1]),
          display: "flex",
          alignItems: "center",
          gap: "24px",
          marginBottom: "48px",
        }}
      >
        <Img
          src={staticFile("lyzr-official-logo-white.svg")}
          style={{
            height: "72px",
            objectFit: "contain",
          }}
        />
        <span
          style={{
            fontFamily: "'Playfair Display', Georgia, serif",
            fontStyle: "italic",
            fontSize: "52px",
            color: "#E05638",
            fontWeight: 700,
          }}
        >
          University
        </span>
      </div>

      {/* 2. Big Clean Hero CTA Title */}
      <div
        style={{
          opacity: linksOpacity,
          fontFamily: "'Playfair Display', Georgia, serif",
          fontStyle: "italic",
          fontSize: "64px",
          color: "#FFFFFF",
          fontWeight: 700,
          marginBottom: "52px",
          lineHeight: 1.2,
        }}
      >
        Build Production-Ready Autonomous AI Agents
      </div>

      {/* 3. Link Pills */}
      <div
        style={{
          opacity: linksOpacity,
          display: "flex",
          gap: "28px",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <div
          style={{
            backgroundColor: "rgba(255, 255, 255, 0.08)",
            border: "1px solid rgba(255, 255, 255, 0.16)",
            borderRadius: "50px",
            padding: "16px 36px",
            color: "#FFFFFF",
            fontSize: "22px",
            fontWeight: 600,
          }}
        >
          🌐 lyzr.ai
        </div>

        <div
          style={{
            backgroundColor: "rgba(224, 86, 56, 0.15)",
            border: "1px solid rgba(224, 86, 56, 0.4)",
            borderRadius: "50px",
            padding: "16px 36px",
            color: "#E05638",
            fontSize: "22px",
            fontWeight: 700,
          }}
        >
          🚀 studio.lyzr.ai
        </div>

        <div
          style={{
            backgroundColor: "rgba(255, 255, 255, 0.08)",
            border: "1px solid rgba(255, 255, 255, 0.16)",
            borderRadius: "50px",
            padding: "16px 36px",
            color: "#FFFFFF",
            fontSize: "22px",
            fontWeight: 600,
          }}
        >
          📖 docs.lyzr.ai
        </div>
      </div>
    </AbsoluteFill>
  );
};
