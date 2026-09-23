import React from "react";
import { AbsoluteFill, Img, staticFile } from "remotion";

export const PersistentBrandFrame: React.FC = () => {
  return (
    <AbsoluteFill
      style={{
        pointerEvents: "none",
        boxSizing: "border-box",
      }}
    >
      {/* 1. Subtle Brand Outline Frame Border */}
      <div
        style={{
          position: "absolute",
          top: 0,
          left: 0,
          right: 0,
          bottom: 0,
          border: "4px solid rgba(113, 81, 79, 0.4)",
          borderRadius: "8px",
          boxSizing: "border-box",
          pointerEvents: "none",
        }}
      />

      {/* 2. Top-Right Persistent Watermark Badge */}
      <div
        style={{
          position: "absolute",
          top: "24px",
          right: "32px",
          display: "flex",
          alignItems: "center",
          gap: "10px",
          backgroundColor: "rgba(18, 15, 14, 0.65)",
          backdropFilter: "blur(12px)",
          border: "1px solid rgba(255, 255, 255, 0.15)",
          padding: "6px 14px",
          borderRadius: "12px",
          opacity: 0.85,
        }}
      >
        <Img
          src={staticFile("lyzr-official-logo-white.svg")}
          style={{ height: "18px", objectFit: "contain" }}
        />
        <span
          style={{
            fontFamily: "'Playfair Display', Georgia, serif",
            fontStyle: "italic",
            fontSize: "14px",
            color: "#C86D51",
            fontWeight: 700,
          }}
        >
          University
        </span>
      </div>
    </AbsoluteFill>
  );
};
