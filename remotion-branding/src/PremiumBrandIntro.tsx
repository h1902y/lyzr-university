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

export interface PremiumIntroProps {
  title?: string;
  subtitle?: string;
}

export const PremiumBrandIntro: React.FC<PremiumIntroProps> = ({
  title = "Enterprise Agent Platform",
  subtitle = "Master Courses · Autonomous AI Workflows",
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Damped spring physics for smooth logo and card entrance
  const cardSpring = spring({
    frame,
    fps,
    config: { damping: 14, stiffness: 120, mass: 0.7 },
  });

  const logoSpring = spring({
    frame: frame - 3,
    fps,
    config: { damping: 12, stiffness: 140, mass: 0.6 },
  });

  const textSpring = spring({
    frame: frame - 6,
    fps,
    config: { damping: 14, stiffness: 110, mass: 0.6 },
  });

  // Glowing pulse animation
  const glowPulse = interpolate(frame, [0, 45, 90, 135], [0.3, 0.6, 0.3, 0.5], {
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
      {/* High-Tech Whoosh & Impact Sound Design */}
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

      {/* Glassmorphic Branded Hero Capsule */}
      <div
        style={{
          transform: `scale(${interpolate(cardSpring, [0, 1], [0.92, 1])})`,
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
        {/* Top Monospace Badge */}
        <div
          style={{
            opacity: interpolate(logoSpring, [0, 1], [0, 1]),
            backgroundColor: "rgba(224, 86, 56, 0.15)",
            border: "1px solid rgba(224, 86, 56, 0.35)",
            borderRadius: "100px",
            padding: "8px 24px",
            color: "#E05638",
            fontSize: "16px",
            fontWeight: 700,
            letterSpacing: "2px",
            textTransform: "uppercase",
            marginBottom: "40px",
          }}
        >
          LYZR UNIVERSITY · OFFICIAL COURSE SERIES
        </div>

        {/* Pure White Lyzr Logo + University Tag */}
        <div
          style={{
            transform: `scale(${interpolate(logoSpring, [0, 1], [0.94, 1])})`,
            opacity: interpolate(logoSpring, [0, 1], [0, 1]),
            display: "flex",
            alignItems: "center",
            gap: "24px",
            marginBottom: "36px",
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

        {/* Hero Title */}
        <div
          style={{
            transform: `scale(${interpolate(textSpring, [0, 1], [0.96, 1])})`,
            opacity: interpolate(textSpring, [0, 1], [0, 1]),
            fontFamily: "'Playfair Display', Georgia, serif",
            fontStyle: "italic",
            fontSize: "76px",
            color: "#FFFFFF",
            fontWeight: 800,
            lineHeight: 1.18,
            maxWidth: "1400px",
            letterSpacing: "-0.5px",
            marginBottom: "24px",
          }}
        >
          {title}
        </div>

        {/* Subtitle */}
        <div
          style={{
            opacity: interpolate(textSpring, [0, 1], [0, 1]),
            fontSize: "26px",
            color: "rgba(255, 255, 255, 0.65)",
            fontWeight: 500,
            letterSpacing: "1px",
          }}
        >
          {subtitle}
        </div>
      </div>
    </AbsoluteFill>
  );
};
