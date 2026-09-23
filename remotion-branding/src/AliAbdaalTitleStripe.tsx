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

export interface AliAbdaalStripeProps {
  title?: string;
  subtitle?: string;
  lessonNum?: string;
}

export const AliAbdaalTitleStripe: React.FC<AliAbdaalStripeProps> = ({
  title = "Designing Knowledge Bases & Source Selection",
  subtitle = "Lyzr Foundation (New)",
  lessonNum = "02",
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  // Ali Abdaal Signature Smooth Slide & Scale Entrance (0 to 18 frames)
  const slideX = spring({
    frame,
    fps,
    config: { damping: 14, stiffness: 140, mass: 0.6 },
  });

  const fadeOpacity = interpolate(frame, [0, 12], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  // Exit animation (fades out gracefully after 4 seconds / 120 frames)
  const exitOpacity = interpolate(frame, [110, 130], [1, 0], {
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
        padding: "80px",
        boxSizing: "border-box",
        opacity: exitOpacity,
      }}
    >
      {/* Signature Ali Abdaal Lower-Third Floating Glass Title Banner */}
      <div
        style={{
          transform: `translateX(${interpolate(slideX, [0, 1], [-100, 0])}px) scale(${interpolate(slideX, [0, 1], [0.9, 1])})`,
          opacity: fadeOpacity,
          backgroundColor: "rgba(18, 15, 14, 0.94)",
          backdropFilter: "blur(20px)",
          borderLeft: "6px solid #C86D51",
          borderRadius: "16px",
          padding: "24px 36px",
          boxShadow: "0 20px 40px rgba(0, 0, 0, 0.6), 0 0 25px rgba(200, 109, 81, 0.2)",
          display: "flex",
          flexDirection: "column",
          gap: "8px",
          maxWidth: "1100px",
        }}
      >
        {/* Top Header Row: White Lyzr Logo + Lesson Pill */}
        <div style={{ display: "flex", alignItems: "center", gap: "16px" }}>
          <Img
            src={staticFile("lyzr-official-logo-white.svg")}
            style={{ height: "28px", objectFit: "contain" }}
          />
          <span
            style={{
              fontFamily: "'Playfair Display', Georgia, serif",
              fontStyle: "italic",
              fontSize: "22px",
              color: "#C86D51",
              fontWeight: 700,
            }}
          >
            University
          </span>
          <span
            style={{
              backgroundColor: "rgba(200, 109, 81, 0.25)",
              color: "#F3EFEA",
              border: "1px solid rgba(200, 109, 81, 0.5)",
              padding: "2px 10px",
              borderRadius: "12px",
              fontSize: "12px",
              fontWeight: 800,
              letterSpacing: "1.5px",
              textTransform: "uppercase",
            }}
          >
            LESSON {lessonNum}
          </span>
        </div>

        {/* Big Bold Clean Lesson Title */}
        <div
          style={{
            fontFamily: "'Playfair Display', Georgia, serif",
            fontStyle: "italic",
            fontSize: "44px",
            color: "#FFFFFF",
            fontWeight: 800,
            lineHeight: 1.2,
            letterSpacing: "-0.3px",
          }}
        >
          {title}
        </div>
      </div>
    </AbsoluteFill>
  );
};
