import React from "react";
import {
  AbsoluteFill,
  Img,
  Audio,
  interpolate,
  spring,
  useCurrentFrame,
  useVideoConfig,
  staticFile,
} from "remotion";

export const PremiumBrandOutro: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Fast 2-second (60 frames) spring physics
  const cardSpring = spring({
    frame,
    fps,
    config: { damping: 12, stiffness: 160, mass: 0.5 },
  });

  const contentSpring = spring({
    frame: frame - 2,
    fps,
    config: { damping: 12, stiffness: 140, mass: 0.5 },
  });

  const glowPulse = interpolate(frame, [0, 30, 60], [0.3, 0.65, 0.4], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill
      style={{
        backgroundColor: "#040404",
        display: "flex",
        alignItems: "center",
        justifyContent: "center",
        boxSizing: "border-box",
        padding: "60px",
        fontFamily: "'Inter', system-ui, -apple-system, sans-serif",
      }}
    >
      {/* High-Tech Outro Audio Sound Effect */}
      <Audio src={staticFile("whoosh_audio.mp3")} />

      {/* Ambient Dark Gradient Radial Backlight */}
      <div
        style={{
          position: "absolute",
          width: "1200px",
          height: "1200px",
          borderRadius: "50%",
          background: `radial-gradient(circle, rgba(224, 86, 56, ${glowPulse}) 0%, rgba(0,0,0,0) 65%)`,
          filter: "blur(90px)",
          pointerEvents: "none",
        }}
      />

      {/* Glassmorphic Outro Hero Capsule */}
      <div
        style={{
          transform: `scale(${interpolate(cardSpring, [0, 1], [0.93, 1])})`,
          opacity: interpolate(cardSpring, [0, 1], [0, 1]),
          width: "1680px",
          height: "880px",
          backgroundColor: "rgba(18, 18, 20, 0.75)",
          backdropFilter: "blur(32px)",
          borderRadius: "32px",
          border: "1.5px solid rgba(224, 86, 56, 0.45)",
          boxShadow: `0 24px 80px rgba(0, 0, 0, 0.8), 0 0 120px rgba(224, 86, 56, ${glowPulse * 0.8})`,
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "center",
          textAlign: "center",
          padding: "60px 80px",
          boxSizing: "border-box",
          position: "relative",
          zIndex: 2,
        }}
      >
        {/* White Lyzr Logo + University Tag */}
        <div
          style={{
            transform: `scale(${interpolate(contentSpring, [0, 1], [0.94, 1])})`,
            opacity: interpolate(contentSpring, [0, 1], [0, 1]),
            display: "flex",
            alignItems: "center",
            gap: "24px",
            marginBottom: "40px",
          }}
        >
          <Img
            src={staticFile("lyzr-official-logo-white.svg")}
            style={{
              height: "76px",
              objectFit: "contain",
            }}
          />
          <span
            style={{
              fontFamily: "'Playfair Display', Georgia, serif",
              fontStyle: "italic",
              fontSize: "56px",
              color: "#E05638",
              fontWeight: 700,
            }}
          >
            University
          </span>
        </div>

        {/* Hero CTA Title */}
        <div
          style={{
            transform: `scale(${interpolate(contentSpring, [0, 1], [0.96, 1])})`,
            opacity: interpolate(contentSpring, [0, 1], [0, 1]),
            fontFamily: "'Playfair Display', Georgia, serif",
            fontStyle: "italic",
            fontSize: "68px",
            color: "#FFFFFF",
            fontWeight: 800,
            lineHeight: 1.18,
            maxWidth: "1400px",
            letterSpacing: "-0.5px",
            marginBottom: "52px",
          }}
        >
          Build Production-Ready Autonomous AI Agents
        </div>

        {/* Branded Link Pills */}
        <div
          style={{
            opacity: interpolate(contentSpring, [0, 1], [0, 1]),
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
              backgroundColor: "rgba(224, 86, 56, 0.18)",
              border: "1.5px solid rgba(224, 86, 56, 0.5)",
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
      </div>
    </AbsoluteFill>
  );
};
