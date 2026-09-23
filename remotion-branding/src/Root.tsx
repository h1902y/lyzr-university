import React from "react";
import { Composition } from "remotion";
import "./index.css";
import { IntroBumper } from "./IntroBumper";
import { PremiumBrandIntro } from "./PremiumBrandIntro";
import { PremiumBrandOutro } from "./PremiumBrandOutro";
import { OutroBumper } from "./OutroBumper";
import { TransitionBumper } from "./TransitionBumper";
import { AliAbdaalTitleStripe } from "./AliAbdaalTitleStripe";
import { FireshipCodeBadge } from "./FireshipCodeBadge";
import { PersistentBrandFrame } from "./PersistentBrandFrame";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="PremiumBrandIntro"
        component={PremiumBrandIntro as any}
        durationInFrames={135}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          title: "Enterprise Agent Platform",
          subtitle: "Master Courses · Autonomous AI Workflows",
        }}
      />
      <Composition
        id="PremiumBrandOutro"
        component={PremiumBrandOutro}
        durationInFrames={60}
        fps={30}
        width={1920}
        height={1080}
      />
      <Composition
        id="IntroBumper"
        component={IntroBumper as any}
        durationInFrames={105}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          title: "Enterprise Agent Platform",
          subtitle: "Master Courses · Autonomous AI Workflows",
        }}
      />
      <Composition
        id="AliAbdaalTitleStripe"
        component={AliAbdaalTitleStripe as any}
        durationInFrames={135}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          title: "Designing Knowledge Bases & Source Selection",
          subtitle: "Lyzr Foundation (New)",
          lessonNum: "02",
        }}
      />
      <Composition
        id="PersistentBrandFrame"
        component={PersistentBrandFrame}
        durationInFrames={120}
        fps={30}
        width={1920}
        height={1080}
      />
      <Composition
        id="OutroBumper"
        component={OutroBumper}
        durationInFrames={135}
        fps={30}
        width={1920}
        height={1080}
      />
      <Composition
        id="TransitionBumper"
        component={TransitionBumper as any}
        durationInFrames={75}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          chapterNum: "02",
          chapterTitle: "Enterprise Knowledge Base Masterclass",
        }}
      />
      <Composition
        id="FireshipCodeBadge"
        component={FireshipCodeBadge as any}
        durationInFrames={120}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          codeSnippet: "pip install lyzr-agent-api",
          badgeText: "ADK QUICKSTART",
        }}
      />
    </>
  );
};
