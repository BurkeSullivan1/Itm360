# For Maria 💕

A beautiful, cinematic slideshow website built with Next.js to showcase your most precious memories together.

## ✨ Features

- **Emotional Opening Scene**: A typewriter sequence that sets the mood
- **Auto-Playing Slideshow**: Smooth transitions between photos and videos
- **Touch & Keyboard Controls**: Navigate with swipes, arrows, or spacebar
- **Captions & Subtitles**: Add personal messages to your memories
- **Deep Linking**: Share specific moments with custom URLs
- **Responsive Design**: Beautiful on all devices
- **Accessibility**: Reduced motion support and keyboard navigation

## 🎨 Design

- **Deep Navy** (#0B1220) - Elegant dark background
- **Soft Gold** (#E7C888) - Warm accent color
- **Off-White** (#F7F5EF) - Gentle text color
- **Ken Burns Effect** - Subtle image animations
- **Framer Motion** - Smooth page transitions

## 🚀 Quick Start

1. **Add Your Memories**
   ```bash
   # Add photos and videos to the mariaimg folder
   cp your-photos/* mariaimg/
   ```

2. **Build the Gallery**
   ```bash
   npm run build:gallery
   ```

3. **Start Development**
   ```bash
   npm run dev
   ```

4. **Open Your Heart**
   Visit [http://localhost:3000](http://localhost:3000)

## 📝 Customization

### Adding Captions
Edit `content/captions.json`:
```json
{
  "photo1.jpg": "The moment I knew I was falling for you ❤️",
  "video1.mp4": "Your laugh in this video still makes my heart skip"
}
```

### Rotating Subtitles
Add sweet whispers in `content/subtitles.json`:
```json
[
  "I still smile at this one",
  "Our song on the radio",
  "You make ordinary moments magical"
]
```

### Background Music
Add `intro.mp3` to `public/audio/` for ambient background music.

## 🛠️ Development

```bash
# Install dependencies
npm install

# Process new media files
npm run build:gallery

# Start development server
npm run dev

# Build for production
npm run build

# Start production server
npm start
```

## 📂 Project Structure

```
├── mariaimg/           # Your photos and videos go here
├── content/
│   ├── gallery.json    # Generated media metadata
│   ├── captions.json   # Your love notes
│   └── subtitles.json  # Rotating whispers
├── src/
│   ├── app/
│   │   ├── page.tsx    # Main application
│   │   └── globals.css # Global styles
│   ├── components/
│   │   ├── OpeningScene.tsx
│   │   ├── Slideshow.tsx
│   │   ├── Lightbox.tsx
│   │   └── Controls.tsx
│   └── lib/
│       └── gallery.ts  # Gallery utilities
├── scripts/
│   └── build-gallery.ts # Media processing script
└── public/
    └── audio/          # Background music
```

## 🌟 Special Features

- **Cold Open**: Emotional text sequence before the slideshow
- **Auto-Advance**: Smart timing based on content type
- **Gallery View**: Optional masonry grid with lightbox
- **Share Links**: Deep links to specific moments (/#/m/5)
- **Sound Toggle**: Optional background music
- **Mobile Optimized**: Touch gestures and responsive design

## 💝 Built with Love

This project uses:
- [Next.js 14](https://nextjs.org/) - React framework
- [Framer Motion](https://www.framer.com/motion/) - Beautiful animations
- [Tailwind CSS](https://tailwindcss.com/) - Utility-first styling
- [Sharp](https://sharp.pixelplumbing.com/) - Image processing
- [TypeScript](https://www.typescriptlang.org/) - Type safety

---

*"Every photo tells a story, every moment matters"* ✨
