+++
title = "Rockkie's Room"
date = "2026-07-27T00:00:00+08:00"
draft = false
description = "A small interactive room built from the things that matter to me."
ShowToc = false
hidemeta = true
ShowReadingTime = false
ShowBreadCrumbs = false
+++

<style>
  .main {
    max-width: min(1120px, calc(100% - var(--gap) * 2));
  }

  .post-content {
    max-width: none;
  }

  .room-page {
    --room-wall: #f4efe7;
    --room-floor: #cda77a;
    --room-line: #3b342f;
    --room-soft: #fffaf3;
    --room-accent: #6f42c1;
    --room-green: #40c463;
    --room-blue: #1d428a;
    --room-gold: #fdb927;
    --room-shadow: rgba(43, 35, 29, 0.18);
    color: var(--primary);
  }

  [data-theme="dark"] .room-page {
    --room-wall: #22283b;
    --room-floor: #46382f;
    --room-line: #e3e8f1;
    --room-soft: #171b29;
    --room-accent: #bb9af7;
    --room-green: #73daca;
    --room-blue: #7aa2f7;
    --room-gold: #e0af68;
    --room-shadow: rgba(0, 0, 0, 0.35);
  }

  .room-intro {
    display: flex;
    align-items: flex-end;
    justify-content: space-between;
    gap: 24px;
    margin-bottom: 18px;
  }

  .room-intro p {
    margin: 0;
    max-width: 650px;
    color: var(--secondary);
  }

  .room-key {
    flex: 0 0 auto;
    padding: 7px 11px;
    border: 1px solid var(--border);
    border-radius: 999px;
    font-size: 0.82rem;
    color: var(--secondary);
    background: var(--entry);
  }

  .room-scene {
    position: relative;
    width: 100%;
    aspect-ratio: 16 / 9;
    overflow: hidden;
    border: 2px solid var(--room-line);
    border-radius: 18px;
    background:
      linear-gradient(to bottom, transparent 0 68%, rgba(0, 0, 0, 0.06) 68% 69%, transparent 69%),
      linear-gradient(to bottom, var(--room-wall) 0 69%, var(--room-floor) 69% 100%);
    box-shadow: 0 18px 45px var(--room-shadow);
    isolation: isolate;
  }

  .room-scene::after {
    content: "";
    position: absolute;
    inset: 69% 0 auto;
    height: 2.5%;
    background: rgba(255, 255, 255, 0.28);
    border-top: 2px solid var(--room-line);
    border-bottom: 1px solid rgba(0, 0, 0, 0.12);
    z-index: 1;
  }

  .window {
    position: absolute;
    left: 7%;
    top: 10%;
    width: 20%;
    height: 35%;
    border: 5px solid var(--room-line);
    border-radius: 5px;
    background: linear-gradient(#8fc9ff 0 55%, #dbeeff 55% 100%);
    box-shadow: inset 0 0 0 4px rgba(255, 255, 255, 0.42);
    z-index: 2;
  }

  [data-theme="dark"] .window {
    background: linear-gradient(#141b35 0 55%, #253457 55% 100%);
  }

  .window::before,
  .window::after {
    content: "";
    position: absolute;
    background: var(--room-line);
  }

  .window::before {
    left: 48%;
    top: 0;
    width: 4%;
    height: 100%;
  }

  .window::after {
    left: 0;
    top: 47%;
    width: 100%;
    height: 5%;
  }

  .city {
    position: absolute;
    left: 10%;
    right: 8%;
    bottom: 4%;
    height: 28%;
    opacity: 0.5;
    background:
      linear-gradient(to right,
        #536274 0 12%, transparent 12% 16%,
        #46576a 16% 31%, transparent 31% 35%,
        #52657a 35% 48%, transparent 48% 52%,
        #43566d 52% 68%, transparent 68% 73%,
        #50647a 73% 100%);
  }

  .star {
    position: absolute;
    width: 5px;
    height: 5px;
    border-radius: 50%;
    background: #fff5bd;
    opacity: 0;
  }

  [data-theme="dark"] .star {
    opacity: 0.85;
    animation: room-twinkle 2.6s ease-in-out infinite;
  }

  .star-one { left: 18%; top: 18%; }
  .star-two { right: 20%; top: 23%; animation-delay: 0.8s; }

  .bed {
    position: absolute;
    right: 5%;
    bottom: 10%;
    width: 36%;
    height: 25%;
    border: 4px solid var(--room-line);
    border-radius: 10px 10px 5px 5px;
    background: #d8d2ee;
    z-index: 3;
  }

  [data-theme="dark"] .bed {
    background: #414766;
  }

  .bed::before {
    content: "";
    position: absolute;
    left: 4%;
    top: 9%;
    width: 28%;
    height: 37%;
    border: 2px solid var(--room-line);
    border-radius: 45%;
    background: #fbfaf6;
  }

  [data-theme="dark"] .bed::before {
    background: #d5d8e3;
  }

  .bed::after {
    content: "";
    position: absolute;
    left: -4px;
    right: -4px;
    bottom: -12%;
    height: 14%;
    border: 4px solid var(--room-line);
    border-top: 0;
    background: #81654d;
  }

  .desk {
    position: absolute;
    left: 29%;
    bottom: 12%;
    width: 31%;
    height: 6%;
    border: 4px solid var(--room-line);
    background: #a8754d;
    z-index: 4;
  }

  .desk::before,
  .desk::after {
    content: "";
    position: absolute;
    top: 100%;
    width: 7%;
    height: 310%;
    border: 3px solid var(--room-line);
    border-top: 0;
    background: #8a5d3f;
  }

  .desk::before { left: 5%; }
  .desk::after { right: 5%; }

  .chair {
    position: absolute;
    left: 38%;
    bottom: 4%;
    width: 11%;
    height: 18%;
    border: 4px solid var(--room-line);
    border-radius: 45% 45% 5px 5px;
    background: #607089;
    z-index: 3;
  }

  .room-object {
    position: absolute;
    z-index: 7;
    display: block;
    color: inherit;
    text-decoration: none;
    cursor: pointer;
    transition: transform 160ms ease, filter 160ms ease;
    outline-offset: 6px;
  }

  .room-object:hover,
  .room-object:focus-visible {
    transform: translateY(-3px) scale(1.045);
    filter: drop-shadow(0 0 8px color-mix(in srgb, var(--room-accent) 62%, transparent));
  }

  .room-tooltip {
    position: absolute;
    left: 50%;
    bottom: calc(100% + 10px);
    width: max-content;
    max-width: 210px;
    padding: 8px 10px;
    border: 1px solid rgba(255, 255, 255, 0.2);
    border-radius: 9px;
    background: rgba(13, 17, 23, 0.94);
    color: #fff;
    font-size: 0.8rem;
    line-height: 1.35;
    text-align: center;
    opacity: 0;
    pointer-events: none;
    transform: translate(-50%, 6px);
    transition: opacity 150ms ease, transform 150ms ease;
    box-shadow: 0 8px 20px rgba(0, 0, 0, 0.22);
  }

  .room-tooltip strong,
  .room-tooltip small {
    display: block;
  }

  .room-tooltip small {
    margin-top: 2px;
    color: #d4d8e0;
  }

  .room-object:hover .room-tooltip,
  .room-object:focus-visible .room-tooltip {
    opacity: 1;
    transform: translate(-50%, 0);
  }

  .jersey {
    left: 44%;
    top: 9%;
    width: 13%;
    height: 29%;
  }

  .jersey-shape {
    position: absolute;
    inset: 0 17% 0;
    border: 4px solid var(--room-line);
    border-radius: 15% 15% 8% 8%;
    background: var(--room-blue);
    color: var(--room-gold);
    text-align: center;
    font-weight: 800;
  }

  .jersey-shape::before,
  .jersey-shape::after {
    content: "";
    position: absolute;
    top: 5%;
    width: 39%;
    height: 28%;
    border: 4px solid var(--room-line);
    background: var(--room-blue);
    z-index: -1;
  }

  .jersey-shape::before {
    right: 81%;
    transform: rotate(24deg);
  }

  .jersey-shape::after {
    left: 81%;
    transform: rotate(-24deg);
  }

  .jersey-name {
    display: block;
    margin-top: 26%;
    font-size: clamp(7px, 1.15vw, 14px);
    letter-spacing: 0.08em;
  }

  .jersey-number {
    display: block;
    margin-top: -3%;
    font-size: clamp(21px, 4vw, 48px);
    line-height: 1;
  }

  .bookshelf {
    left: 4%;
    bottom: 13%;
    width: 19%;
    height: 43%;
    border: 4px solid var(--room-line);
    background: #8a5c3e;
  }

  .shelf-row {
    position: relative;
    display: flex;
    align-items: flex-end;
    gap: 4%;
    height: 33.333%;
    padding: 7% 7% 4%;
    border-bottom: 4px solid var(--room-line);
  }

  .shelf-row:last-child {
    border-bottom: 0;
  }

  .book {
    display: block;
    width: 14%;
    border: 2px solid var(--room-line);
    border-radius: 2px 2px 0 0;
  }

  .book:nth-child(1) { height: 78%; background: #e76f51; }
  .book:nth-child(2) { height: 92%; background: #2a9d8f; }
  .book:nth-child(3) { height: 68%; background: #e9c46a; }
  .book:nth-child(4) { height: 86%; background: #7b6dce; }
  .book:nth-child(5) { height: 74%; background: #5da271; }

  .basketball {
    right: 28%;
    bottom: 4%;
    width: 8%;
    aspect-ratio: 1;
    border: 4px solid var(--room-line);
    border-radius: 50%;
    background:
      linear-gradient(24deg, transparent 46%, var(--room-line) 47% 52%, transparent 53%),
      linear-gradient(156deg, transparent 46%, var(--room-line) 47% 52%, transparent 53%),
      radial-gradient(circle at 50% 0, transparent 42%, var(--room-line) 43% 48%, transparent 49%),
      #de7b2d;
  }

  .dumbbell {
    left: 26%;
    bottom: 4.5%;
    width: 13%;
    height: 6%;
  }

  .dumbbell-bar {
    position: absolute;
    left: 12%;
    right: 12%;
    top: 38%;
    height: 24%;
    border: 2px solid var(--room-line);
    background: #b8bec9;
  }

  .dumbbell::before,
  .dumbbell::after {
    content: "";
    position: absolute;
    top: 0;
    width: 18%;
    height: 100%;
    border: 3px solid var(--room-line);
    border-radius: 5px;
    background: #3d4450;
  }

  .dumbbell::before { left: 0; }
  .dumbbell::after { right: 0; }

  .roller {
    left: 41%;
    bottom: 2.5%;
    width: 14%;
    height: 5.5%;
    border: 3px solid var(--room-line);
    border-radius: 999px;
    background: repeating-linear-gradient(90deg, #7b6dce 0 9%, #9d91e5 9% 17%);
    transform: rotate(-5deg);
  }

  .roller:hover,
  .roller:focus-visible {
    transform: rotate(-5deg) translateY(-3px) scale(1.045);
  }

  .cd-player {
    left: 43%;
    bottom: 24%;
    width: 12%;
    height: 9%;
    border: 3px solid var(--room-line);
    border-radius: 6px;
    background: #d6d9df;
  }

  .cd-disc {
    position: absolute;
    left: 8%;
    top: 15%;
    width: 38%;
    aspect-ratio: 1;
    border: 2px solid var(--room-line);
    border-radius: 50%;
    background: conic-gradient(#7b6dce, #73daca, #f2cc60, #e76f51, #7b6dce);
    animation: room-spin 8s linear infinite;
  }

  .cd-disc::after {
    content: "";
    position: absolute;
    inset: 36%;
    border: 1px solid var(--room-line);
    border-radius: 50%;
    background: #f5f5f5;
  }

  .cd-controls {
    position: absolute;
    right: 8%;
    top: 25%;
    width: 34%;
    height: 13%;
    border-radius: 3px;
    background: #434a57;
    box-shadow: 0 12px 0 -4px #606978;
  }

  .story-grid {
    display: grid;
    grid-template-columns: repeat(2, minmax(0, 1fr));
    gap: 16px;
    margin-top: 34px;
  }

  .story-card {
    scroll-margin-top: 90px;
    min-height: 170px;
    padding: 20px;
    border: 1px solid var(--border);
    border-radius: 14px;
    background: var(--entry);
  }

  .story-card h2 {
    margin: 8px 0 8px;
    font-size: 1.2rem;
  }

  .story-card p {
    margin: 0;
    color: var(--secondary);
  }

  .story-card:target {
    border-color: var(--room-accent);
    box-shadow: 0 0 0 3px color-mix(in srgb, var(--room-accent) 18%, transparent);
  }

  .story-status {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    padding: 4px 8px;
    border-radius: 999px;
    color: var(--room-accent);
    background: color-mix(in srgb, var(--room-accent) 12%, transparent);
    font-size: 0.76rem;
    font-weight: 600;
  }

  .story-link {
    display: inline-block;
    margin-top: 14px;
    color: var(--room-accent);
    font-size: 0.88rem;
    font-weight: 600;
  }

  .library-card {
    grid-column: 1 / -1;
    min-height: 190px;
    border-style: dashed;
  }

  .library-preview {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 10px;
    margin-top: 16px;
  }

  .library-preview span {
    display: block;
    height: 9px;
    border-radius: 999px;
    background: var(--border);
  }

  .library-preview span:nth-child(1) { width: 86%; background: var(--room-green); }
  .library-preview span:nth-child(2) { width: 58%; background: var(--room-accent); }
  .library-preview span:nth-child(3) { width: 72%; background: var(--room-gold); }

  @keyframes room-spin {
    to { transform: rotate(360deg); }
  }

  @keyframes room-twinkle {
    0%, 100% { transform: scale(0.7); opacity: 0.35; }
    50% { transform: scale(1.3); opacity: 1; }
  }

  @media (max-width: 720px) {
    .main {
      max-width: calc(100% - var(--gap) * 2);
    }

    .room-intro {
      align-items: flex-start;
      flex-direction: column;
      gap: 10px;
    }

    .room-key {
      font-size: 0.72rem;
    }

    .room-scene {
      border-radius: 12px;
    }

    .room-tooltip {
      display: none;
    }

    .story-grid {
      grid-template-columns: 1fr;
    }

    .library-card {
      grid-column: auto;
    }
  }

  @media (prefers-reduced-motion: reduce) {
    .room-page *,
    .room-page *::before,
    .room-page *::after {
      animation-duration: 0.01ms !important;
      animation-iteration-count: 1 !important;
      scroll-behavior: auto !important;
      transition-duration: 0.01ms !important;
    }
  }
</style>

<div class="room-page">
  <div class="room-intro">
    <p>
      A small room made from the things that matter to me. Hover over an object to discover its story, then click to open the first placeholder for that chapter.
    </p>
    <span class="room-key">Hover or tap the objects</span>
  </div>

  <div class="room-scene" role="img" aria-label="An interactive bedroom with a Curry jersey, basketball, dumbbell, foam roller, CD player, desk, bed, window and bookshelf.">
    <div class="window" aria-hidden="true">
      <span class="star star-one"></span>
      <span class="star star-two"></span>
      <span class="city"></span>
    </div>

    <div class="bed" aria-hidden="true"></div>
    <div class="desk" aria-hidden="true"></div>
    <div class="chair" aria-hidden="true"></div>

    <a class="room-object jersey" href="#idol" aria-label="Open the story about Stephen Curry as an idol">
      <span class="jersey-shape" aria-hidden="true">
        <span class="jersey-name">CURRY</span>
        <span class="jersey-number">30</span>
      </span>
      <span class="room-tooltip">
        <strong>Stephen Curry Jersey</strong>
        <small>About the person who inspired me</small>
      </span>
    </a>

    <a class="room-object bookshelf" href="#library" aria-label="Open the future reading shelf and PDF library">
      <span class="shelf-row" aria-hidden="true">
        <span class="book"></span><span class="book"></span><span class="book"></span><span class="book"></span><span class="book"></span>
      </span>
      <span class="shelf-row" aria-hidden="true">
        <span class="book"></span><span class="book"></span><span class="book"></span><span class="book"></span><span class="book"></span>
      </span>
      <span class="shelf-row" aria-hidden="true">
        <span class="book"></span><span class="book"></span><span class="book"></span><span class="book"></span><span class="book"></span>
      </span>
      <span class="room-tooltip">
        <strong>Reading Shelf</strong>
        <small>Papers, books, PDFs and notes</small>
      </span>
    </a>

    <a class="room-object basketball" href="#basketball" aria-label="Open the story about basketball">
      <span class="room-tooltip">
        <strong>Basketball</strong>
        <small>More than a sport</small>
      </span>
    </a>

    <a class="room-object dumbbell" href="#fitness" aria-label="Open the story about fitness and training">
      <span class="dumbbell-bar" aria-hidden="true"></span>
      <span class="room-tooltip">
        <strong>Training</strong>
        <small>Building strength one session at a time</small>
      </span>
    </a>

    <a class="room-object roller" href="#injury" aria-label="Open the story about injury and recovery">
      <span class="room-tooltip">
        <strong>Recovery</strong>
        <small>The injury that changed how I train</small>
      </span>
    </a>

    <a class="room-object cd-player" href="#music" aria-label="Open the story about music">
      <span class="cd-disc" aria-hidden="true"></span>
      <span class="cd-controls" aria-hidden="true"></span>
      <span class="room-tooltip">
        <strong>CD Player</strong>
        <small>Music I keep coming back to</small>
      </span>
    </a>
  </div>

  <div class="story-grid" aria-label="Story placeholders">
    <section class="story-card" id="idol">
      <span class="story-status">Story placeholder</span>
      <h2>Idol — Stephen Curry</h2>
      <p>This page will hold a personal essay about admiration, influence and what Curry's journey means to me beyond basketball.</p>
      <a class="story-link" href="#top">Return to the room ↑</a>
    </section>

    <section class="story-card" id="basketball">
      <span class="story-status">Story placeholder</span>
      <h2>Passion — Basketball</h2>
      <p>This chapter will be about the sport itself: why I love it, how it stays in my life and the memories attached to it.</p>
      <a class="story-link" href="#top">Return to the room ↑</a>
    </section>

    <section class="story-card" id="fitness">
      <span class="story-status">Story placeholder</span>
      <h2>Fitness — Training</h2>
      <p>This chapter will collect my evolving relationship with strength, consistency and the process of becoming physically stronger.</p>
      <a class="story-link" href="#top">Return to the room ↑</a>
    </section>

    <section class="story-card" id="injury">
      <span class="story-status">Story placeholder</span>
      <h2>Recovery — My Injury Story</h2>
      <p>This chapter will tell the more difficult story: injury, frustration, rehabilitation and what recovery changed in my understanding of training.</p>
      <a class="story-link" href="#top">Return to the room ↑</a>
    </section>

    <section class="story-card" id="music">
      <span class="story-status">Story placeholder</span>
      <h2>Music — What I Listen To</h2>
      <p>This chapter will become a small listening room for albums, songs and the memories or phases of life connected to them.</p>
      <a class="story-link" href="#top">Return to the room ↑</a>
    </section>

    <section class="story-card library-card" id="library">
      <span class="story-status">Future system</span>
      <h2>Reading Shelf — PDF Library</h2>
      <p>The bookshelf is reserved for a future reading system that connects papers, PDFs, reading notes, progress and reading-time statistics. The first version will eventually surface a small public collection from Zotero rather than duplicate the entire library.</p>
      <div class="library-preview" aria-hidden="true">
        <span></span><span></span><span></span>
      </div>
      <a class="story-link" href="#top">Return to the room ↑</a>
    </section>
  </div>
</div>
