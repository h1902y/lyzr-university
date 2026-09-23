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

export interface TransitionProps {
  lessonNum?: string;
  lessonTitle?: string;
}

export const TransitionBumper: React.FC<TransitionProps> = ({
  lessonNum = "03",
  lessonTitle = "PDF Parsing Strategies & Tabular Data Extraction",
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const titleSpring = spring({
    frame,
    fps,
    config: { damping: 14, stiffness: 140, mass: 0.6 },
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
      <div
        style={{
          transform: `scale(${interpolate(titleSpring, [0, 1], [0.94, 1])})`,
          opacity: interpolate(titleSpring, [0, 1], [0, 1]),
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
        }}
      >
        <div
          style={{
            display: "flex",
            alignItems: "center",
            gap: "16px",
            marginBottom: "28px",
          }}
        >
          <Img src={staticFile("lyzr-official-logomark-white.svg")} style={{ height: "40px" }} />
          <span
            style={{
              color: "#C86D51",
              fontSize: "20px",
              fontWeight: 800,
              letterSpacing: "4px",
              textTransform: "uppercase",
            }}
          >
            LESSON {lessonNum}
          </span>
        </div>

        <div
          style={{
            fontFamily: "'Playfair Display', Georgia, serif",
            fontStyle: "italic",
            fontSize: "64px",
            color: "#FFFFFF",
            fontWeight: 800,
            maxWidth: "1400px",
            lineHeight: 1.2,
          }}
        >
          {lessonTitle}
        </div>
      </div>
    </AbsoluteFill>
  );
};
