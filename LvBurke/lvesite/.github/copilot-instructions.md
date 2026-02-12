<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

# "For Maria" - Cinematic Slideshow Website

This is a Next.js 14 project built with TypeScript, Tailwind CSS, and Framer Motion for creating a beautiful, cinematic slideshow website featuring personal photos and videos.

## Project Structure

- **Opening Scene**: Emotional typewriter sequence that introduces the slideshow
- **Slideshow**: Auto-playing media with smooth transitions, captions, and controls
- **Gallery Grid**: Optional masonry-style grid view with lightbox functionality
- **Media Processing**: Build script that scans local folder and generates gallery metadata

## Key Features

- Responsive design with mobile touch/swipe support
- Keyboard navigation (Space, Arrow keys, Escape)
- Deep linking to specific moments (`/#/m/index`)
- Accessible controls and reduced motion support
- Background audio with user toggle
- Ken Burns effect on images (respects reduced motion preference)

## Color Palette

- Navy: #0B1220 (primary background)
- Gold: #E7C888 (accent color)
- Cream: #F7F5EF (text color)

## Development Commands

- `npm run dev` - Start development server
- `npm run build:gallery` - Process images/videos from mariaimg folder
- `npm run build` - Build for production
- `npm run start` - Start production server

## Content Management

- Add photos/videos to `/mariaimg` folder
- Edit captions in `/content/captions.json`
- Customize subtitle whispers in `/content/subtitles.json`
- Run `npm run build:gallery` to update the gallery

The project emphasizes emotional storytelling through smooth animations, thoughtful typography, and carefully crafted user interactions.
