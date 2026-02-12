'use client';

import { useState, useEffect, useRef } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import Image from 'next/image';
import { MediaItem } from '@/lib/gallery';
import Controls from './Controls';
import PersonalNotes from './PersonalNotes';
import PopupNote from './PopupNote';

interface SlideshowProps {
  items: MediaItem[];
  initialIndex?: number;
  autoPlay?: boolean;
  onIndexChange?: (index: number) => void;
  onRestartIntro?: () => void;
  onSlideshowEnd?: () => void;
}

export default function Slideshow({ 
  items, 
  initialIndex = 0, 
  autoPlay = true,
  onIndexChange,
  onRestartIntro,
  onSlideshowEnd
}: SlideshowProps) {
  const [currentIndex, setCurrentIndex] = useState(initialIndex);
  const [isPlaying, setIsPlaying] = useState(autoPlay);
  const [showNote, setShowNote] = useState(false);
  const videoRef = useRef<HTMLVideoElement>(null);
  const intervalRef = useRef<NodeJS.Timeout | null>(null);

  const currentItem = items[currentIndex];

  // Auto-advance slideshow
  useEffect(() => {
    if (isPlaying && items.length > 1) {
      const duration = currentItem?.type === 'video' ? 
        (currentItem.duration ? currentItem.duration * 1000 : 8000) : 5000;
      
      intervalRef.current = setTimeout(() => {
        if (currentIndex === items.length - 1) {
          // Slideshow completed, trigger outro
          onSlideshowEnd?.();
        } else {
          const newIndex = currentIndex + 1;
          setCurrentIndex(newIndex);
          onIndexChange?.(newIndex);
        }
      }, duration);
    }

    return () => {
      if (intervalRef.current) {
        clearTimeout(intervalRef.current);
      }
    };
  }, [currentIndex, isPlaying, currentItem, items.length, onIndexChange, onSlideshowEnd]);

  // Keyboard controls
  useEffect(() => {
    const handleKeyPress = (event: KeyboardEvent) => {
      switch (event.code) {
        case 'Space':
          event.preventDefault();
          setIsPlaying(!isPlaying);
          break;
        case 'ArrowLeft':
          event.preventDefault();
          const prevIndex = currentIndex === 0 ? items.length - 1 : currentIndex - 1;
          setCurrentIndex(prevIndex);
          onIndexChange?.(prevIndex);
          break;
        case 'ArrowRight':
          event.preventDefault();
          if (currentIndex === items.length - 1) {
            onSlideshowEnd?.();
          } else {
            const nextIndex = currentIndex + 1;
            setCurrentIndex(nextIndex);
            onIndexChange?.(nextIndex);
          }
          break;
      }
    };

    document.addEventListener('keydown', handleKeyPress);
    return () => document.removeEventListener('keydown', handleKeyPress);
  }, [isPlaying, currentIndex, items.length, onIndexChange, onSlideshowEnd]);

  // Touch/swipe support
  useEffect(() => {
    let touchStartX = 0;
    let touchEndX = 0;

    const handleTouchStart = (event: TouchEvent) => {
      touchStartX = event.changedTouches[0].screenX;
    };

    const handleTouchEnd = (event: TouchEvent) => {
      touchEndX = event.changedTouches[0].screenX;
      handleSwipe();
    };

    const handleSwipe = () => {
      const swipeThreshold = 50;
      const diff = touchStartX - touchEndX;

      if (Math.abs(diff) > swipeThreshold) {
        if (diff > 0) {
          // Swipe left (next)
          if (currentIndex === items.length - 1) {
            onSlideshowEnd?.();
          } else {
            const nextIndex = currentIndex + 1;
            setCurrentIndex(nextIndex);
            onIndexChange?.(nextIndex);
          }
        } else {
          // Swipe right (previous)
          const prevIndex = currentIndex === 0 ? items.length - 1 : currentIndex - 1;
          setCurrentIndex(prevIndex);
          onIndexChange?.(prevIndex);
        }
      }
    };

    document.addEventListener('touchstart', handleTouchStart);
    document.addEventListener('touchend', handleTouchEnd);

    return () => {
      document.removeEventListener('touchstart', handleTouchStart);
      document.removeEventListener('touchend', handleTouchEnd);
    };
  }, [currentIndex, items.length, onIndexChange, onSlideshowEnd]);

  const handlePlayPause = () => {
    setIsPlaying(!isPlaying);
    
    if (videoRef.current) {
      if (isPlaying) {
        videoRef.current.pause();
      } else {
        videoRef.current.play();
      }
    }
  };

  const handleShare = async () => {
    try {
      const url = `${window.location.origin}/#/m/${currentIndex}`;
      await navigator.clipboard.writeText(url);
      // You could add a toast notification here
    } catch (error) {
      console.warn('Could not copy to clipboard:', error);
    }
  };

  if (!currentItem) {
    return (
      <div className="fixed inset-0 bg-navy flex items-center justify-center">
        <div className="text-cream text-center">
          <h2 className="text-2xl font-light mb-4">No memories found</h2>
          <p className="text-cream/60">Add photos and videos to the mariaimg folder</p>
        </div>
      </div>
    );
  }

  return (
    <div className="fixed inset-0 bg-gradient-to-br from-navy via-navy/98 to-navy/95 overflow-hidden">
      {/* Main content area with improved layout */}
      <div className="relative w-full h-full flex items-center justify-center p-4">
        <AnimatePresence mode="wait">
          <motion.div
            key={currentIndex}
            className="relative w-full h-full flex items-center justify-center"
            initial={{ opacity: 0, scale: 0.95, y: 20 }}
            animate={{ opacity: 1, scale: 1, y: 0 }}
            exit={{ opacity: 0, scale: 1.05, y: -20 }}
            transition={{ duration: 0.7, ease: "easeOut" }}
          >
            {currentItem.type === 'image' ? (
              <motion.div
                className="relative w-full h-full"
                animate={{ 
                  scale: window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 1 : [1, 1.02, 1]
                }}
                transition={{ 
                  duration: 20, 
                  ease: "easeInOut",
                  repeat: Infinity,
                  repeatType: "reverse"
                }}
              >
                <Image
                  src={currentItem.src}
                  alt={currentItem.caption || `Memory ${currentIndex + 1}`}
                  fill
                  className="object-contain"
                  sizes="100vw"
                  priority={currentIndex <= 2}
                  quality={95}
                />
              </motion.div>
            ) : (
              <video
                ref={videoRef}
                src={currentItem.src}
                className="max-w-full max-h-full object-contain"
                autoPlay={isPlaying}
                muted
                playsInline
                preload="metadata"
                onEnded={() => {
                  if (currentIndex === items.length - 1) {
                    onSlideshowEnd?.();
                  } else {
                    const newIndex = currentIndex + 1;
                    setCurrentIndex(newIndex);
                    onIndexChange?.(newIndex);
                  }
                }}
                onLoadedData={() => {
                  if (videoRef.current && isPlaying) {
                    videoRef.current.play();
                  }
                }}
              />
            )}
          </motion.div>
        </AnimatePresence>

        {/* Subtle vignette effect for improved aesthetics */}
        <div className="absolute inset-0 bg-gradient-to-r from-navy/20 via-transparent to-navy/20 pointer-events-none" />
        <div className="absolute inset-0 bg-gradient-to-t from-navy/30 via-transparent to-navy/30 pointer-events-none" />
      </div>

      {/* Personal Notes on the left (hidden on small screens) */}
      <div className="hidden md:block">
        <PersonalNotes currentIndex={currentIndex} totalItems={items.length} />
      </div>

      {/* Note button on the right */}
      <motion.button
        onClick={() => setShowNote(true)}
        className="fixed right-8 top-1/2 transform -translate-y-1/2 p-4 bg-navy/80 hover:bg-navy/90 border border-gold/30 rounded-full transition-all duration-300 focus:outline-none focus:ring-2 focus:ring-gold/50 z-20 group"
        initial={{ opacity: 0, x: 50 }}
        animate={{ opacity: 1, x: 0 }}
        transition={{ duration: 0.8, delay: 1.2 }}
        whileHover={{ scale: 1.1 }}
        whileTap={{ scale: 0.9 }}
      >
        <svg className="w-6 h-6 text-gold group-hover:text-cream transition-colors" fill="currentColor" viewBox="0 0 20 20">
          <path d="M2 5a2 2 0 012-2h7a2 2 0 012 2v4a2 2 0 01-2 2H9l-3 3v-3H4a2 2 0 01-2-2V5z" />
          <path d="M15 7v2a4 4 0 01-4 4H9.828l-1.766 1.767c.28.149.599.233.938.233h2l3 3v-3h2a2 2 0 002-2V9a2 2 0 00-2-2h-1z" />
        </svg>
      </motion.button>

      {/* Restart Intro Button */}
      {onRestartIntro && (
        <motion.button
          onClick={onRestartIntro}
          className="absolute top-8 left-8 p-3 bg-navy/80 hover:bg-navy/90 border border-gold/30 rounded-full transition-all duration-300 focus:outline-none focus:ring-2 focus:ring-gold/50 z-30 group"
          initial={{ opacity: 0, x: -50 }}
          animate={{ opacity: 1, x: 0 }}
          transition={{ duration: 0.8, delay: 1.2 }}
          whileHover={{ scale: 1.1 }}
          whileTap={{ scale: 0.9 }}
          title="Restart Intro"
        >
          <svg className="w-5 h-5 text-gold group-hover:text-cream transition-colors" fill="currentColor" viewBox="0 0 20 20">
            <path fillRule="evenodd" d="M4 2a1 1 0 011 1v2.101a7.002 7.002 0 0111.601 2.566 1 1 0 11-1.885.666A5.002 5.002 0 005.999 7H9a1 1 0 010 2H4a1 1 0 01-1-1V3a1 1 0 011-1zm.008 9.057a1 1 0 011.276.61A5.002 5.002 0 0014.001 13H11a1 1 0 110-2h5a1 1 0 011 1v5a1 1 0 11-2 0v-2.101a7.002 7.002 0 01-11.601-2.566 1 1 0 01.61-1.276z" clipRule="evenodd" />
          </svg>
        </motion.button>
      )}

      {/* Moments counter (moves down on small screens to avoid notch) */}
      <motion.div
        className="absolute top-6 md:top-8 right-6 md:right-8 text-cream/60 text-xs md:text-sm font-medium z-10"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 1 }}
      >
        {currentIndex + 1} of {items.length}
      </motion.div>

      {/* Controls */}
      {/* Controls with safe-area inset on iOS */}
      <Controls
        isPlaying={isPlaying}
        currentIndex={currentIndex}
        totalItems={items.length}
        onPlayPause={handlePlayPause}
        onPrevious={() => {
          const newIndex = currentIndex === 0 ? items.length - 1 : currentIndex - 1;
          setCurrentIndex(newIndex);
          onIndexChange?.(newIndex);
        }}
        onNext={() => {
          if (currentIndex === items.length - 1) {
            onSlideshowEnd?.();
          } else {
            const newIndex = currentIndex + 1;
            setCurrentIndex(newIndex);
            onIndexChange?.(newIndex);
          }
        }}
        onShare={handleShare}
      />

      {/* Caption overlay for each memory (center bottom, above controls) */}
      {currentItem.caption && (
        <motion.div
          className="fixed left-1/2 -translate-x-1/2 bottom-[calc(env(safe-area-inset-bottom)+5.5rem)] md:bottom-28 z-10 max-w-[92vw] md:max-w-2xl"
          initial={{ opacity: 0, y: 10 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.4, delay: 0.6 }}
        >
          <div className="bg-navy/80 backdrop-blur-sm border border-gold/20 rounded-2xl px-4 py-3 md:px-6 md:py-4 shadow-xl">
            <p className="text-cream/90 text-sm md:text-lg leading-snug md:leading-relaxed text-center">
              {currentItem.caption}
            </p>
          </div>
        </motion.div>
      )}

      {/* Popup Note */}
      <PopupNote 
        isOpen={showNote} 
        onClose={() => setShowNote(false)} 
      />
    </div>
  );
}
