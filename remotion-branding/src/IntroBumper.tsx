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

export interface IntroProps {
  title?: string;
  subtitle?: string;
}

export const IntroBumper: React.FC<IntroProps> = ({
  title = "Enterprise Agent Platform",
  subtitle = "Master Courses · Autonomous AI Workflows",
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const logoSpring = spring({
    frame,
    fps,
    config: { damping: 15, stiffness: 140, mass: 0.6 },
  });

  const titleSpring = spring({
    frame: frame - 4,
    fps,
    config: { damping: 15, stiffness: 120, mass: 0.6 },
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
      {/* Official Pure White Lyzr Logo Header */}
      <div
        style={{
          transform: `scale(${interpolate(logoSpring, [0, 1], [0.94, 1])})`,
          opacity: interpolate(logoSpring, [0, 1], [0, 1]),
          display: "flex",
          alignItems: "center",
          gap: "24px",
          marginBottom: "40px",
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

      {/* Course-Agnostic Hero Title */}
      <div
        style={{
          transform: `scale(${interpolate(titleSpring, [0, 1], [0.96, 1])})`,
          opacity: interpolate(titleSpring, [0, 1], [0, 1]),
          fontFamily: "'Playfair Display', Georgia, serif",
          fontStyle: "italic",
          fontSize: "80px",
          color: "#FFFFFF",
          fontWeight: 800,
          lineHeight: 1.18,
          maxWidth: "1600px",
          letterSpacing: "-0.5px",
          marginBottom: "24px",
        }}
      >
        {title}
      </div>

      {/* Subtitle */}
      <div
        style={{
          opacity: interpolate(titleSpring, [0, 1], [0, 1]),
          fontSize: "28px",
          color: "rgba(255, 255, 255, 0.7)",
          fontWeight: 500,
          letterSpacing: "1px",
        }}
      >
        {subtitle}
      </div>
    </AbsoluteFill>
  );
};
