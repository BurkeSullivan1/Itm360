'use client';

import { useState, useEffect, useRef } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import Image from 'next/image';
import { getGalleryData, MediaItem } from '@/lib/gallery';
import OpeningScene from '@/components/OpeningScene';
import Slideshow from '@/components/Slideshow';
import OutroScene from '@/components/OutroScene';
import Lightbox from '@/components/Lightbox';

export default function HomePage() {
  const [currentView, setCurrentView] = useState<'opening' | 'slideshow' | 'slideshow-only' | 'gallery' | 'outro'>('opening');
  const [galleryData, setGalleryData] = useState<MediaItem[]>([]);
  const [currentIndex, setCurrentIndex] = useState(0);
  const [isSoundEnabled, setIsSoundEnabled] = useState(false);
  const [lightboxOpen, setLightboxOpen] = useState(false);
  const [lightboxIndex, setLightboxIndex] = useState(0);
  const audioRef = useRef<HTMLAudioElement>(null);

  // Load gallery data
  useEffect(() => {
    const loadGallery = async () => {
      try {
        const data = await getGalleryData();
        setGalleryData(data.items);
      } catch (error) {
        console.warn('Could not load gallery data:', error);
      }
    };

    loadGallery();
  }, []);

  // Handle URL hash navigation
  useEffect(() => {
    const handleHashChange = () => {
      const hash = window.location.hash;
      const match = hash.match(/#\/m\/(\d+)/);
      
      if (match) {
        const index = parseInt(match[1], 10);
        if (index >= 0 && index < galleryData.length) {
          setCurrentIndex(index);
          if (currentView === 'opening') {
            setCurrentView('slideshow');
          }
        }
      }
    };

    window.addEventListener('hashchange', handleHashChange);
    handleHashChange(); // Check initial hash

    return () => window.removeEventListener('hashchange', handleHashChange);
  }, [galleryData.length, currentView]);

  const startSlideshow = () => {
    setCurrentView('slideshow');
    if (isSoundEnabled && audioRef.current) {
      audioRef.current.play().catch(console.warn);
    }
  };

  const restartIntro = () => {
    setCurrentView('opening');
    setCurrentIndex(0);
    window.history.replaceState(null, '', '/');
    if (audioRef.current) {
      audioRef.current.pause();
      audioRef.current.currentTime = 0;
    }
  };

  const handleSlideshowEnd = () => {
    setCurrentView('outro');
  };

  const toggleSound = () => {
    setIsSoundEnabled(!isSoundEnabled);
    if (audioRef.current) {
      if (!isSoundEnabled) {
        audioRef.current.play().catch(console.warn);
      } else {
        audioRef.current.pause();
      }
    }
  };

  const handleIndexChange = (index: number) => {
    setCurrentIndex(index);
    window.history.replaceState(null, '', `#/m/${index}`);
  };

  const openLightbox = (index: number) => {
    setLightboxIndex(index);
    setLightboxOpen(true);
  };

  const closeLightbox = () => {
    setLightboxOpen(false);
  };

  // Gallery grid component
  const GalleryGrid = () => (
    <div className="min-h-screen bg-gradient-to-br from-navy via-navy/95 to-navy/90 py-16">
      <div className="container mx-auto px-8">
        <motion.div
          className="text-center mb-12"
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
        >
          <h2 className="text-4xl md:text-5xl font-light text-cream mb-4">
            Our Moments
          </h2>
          <p className="text-cream/70 text-lg">
            A collection of memories we&apos;ve made together
          </p>
          <motion.button
            onClick={() => setCurrentView('slideshow')}
            className="mt-6 mr-4 px-8 py-3 bg-gold/20 hover:bg-gold/30 text-cream border border-gold/40 rounded-2xl font-medium transition-all duration-300 hover:scale-105 focus:outline-none focus:ring-2 focus:ring-gold/50"
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
          >
            View Slideshow
          </motion.button>
          
          <motion.button
            onClick={() => setCurrentView('slideshow-only')}
            className="mt-6 px-8 py-3 bg-navy/40 hover:bg-navy/60 text-cream border border-cream/40 rounded-2xl font-medium transition-all duration-300 hover:scale-105 focus:outline-none focus:ring-2 focus:ring-cream/50"
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
          >
            Slideshow Only
          </motion.button>
        </motion.div>

        <motion.div 
          className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ duration: 0.8, delay: 0.3 }}
        >
          {galleryData.map((item, index) => (
            <motion.div
              key={index}
              className="group relative bg-navy/40 rounded-2xl overflow-hidden border border-gold/10 hover:border-gold/30 transition-all duration-300 cursor-pointer"
              initial={{ opacity: 0, y: 30 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 0.5, delay: index * 0.1 }}
              whileHover={{ scale: 1.02, y: -5 }}
              onClick={() => openLightbox(index)}
            >
              <div className="relative aspect-square">
                {item.type === 'image' ? (
                  <Image
                    src={item.src}
                    alt={item.caption || `Memory ${index + 1}`}
                    fill
                    className="object-cover transition-transform duration-300 group-hover:scale-110"
                    sizes="(max-width: 768px) 100vw, (max-width: 1200px) 50vw, 25vw"
                  />
                ) : (
                  <div className="relative w-full h-full">
                    <video
                      src={item.src}
                      className="w-full h-full object-cover"
                      muted
                      playsInline
                      preload="metadata"
                    />
                    <div className="absolute inset-0 flex items-center justify-center bg-navy/30">
                      <svg className="w-12 h-12 text-cream/80" fill="currentColor" viewBox="0 0 20 20">
                        <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zM9.555 7.168A1 1 0 008 8v4a1 1 0 001.555.832l3-2a1 1 0 000-1.664l-3-2z" clipRule="evenodd" />
                      </svg>
                    </div>
                  </div>
                )}
                
                {/* Overlay */}
                <div className="absolute inset-0 bg-gradient-to-t from-navy/60 via-transparent to-transparent opacity-0 group-hover:opacity-100 transition-opacity duration-300" />
                
                {/* Caption preview */}
                {item.caption && (
                  <div className="absolute bottom-0 left-0 right-0 p-4 text-cream text-sm opacity-0 group-hover:opacity-100 transition-opacity duration-300">
                    <p className="line-clamp-2">{item.caption}</p>
                  </div>
                )}
              </div>
            </motion.div>
          ))}
        </motion.div>
      </div>
    </div>
  );

  return (
    <div className="min-h-screen bg-navy text-cream">
      {/* Background audio */}
      <audio
        ref={audioRef}
        src="/audio/intro.mp3"
        loop
        preload="metadata"
        onError={() => console.warn('Could not load background audio')}
      />

      {/* Main content */}
      <AnimatePresence mode="wait">
        {currentView === 'opening' && (
          <OpeningScene
            key="opening"
            onStart={startSlideshow}
            onToggleSound={toggleSound}
            isSoundEnabled={isSoundEnabled}
          />
        )}

        {(currentView === 'slideshow' || currentView === 'slideshow-only') && galleryData.length > 0 && (
          <Slideshow
            key="slideshow"
            items={galleryData}
            initialIndex={currentIndex}
            onIndexChange={handleIndexChange}
            onRestartIntro={restartIntro}
            onSlideshowEnd={handleSlideshowEnd}
          />
        )}

        {currentView === 'gallery' && (
          <GalleryGrid key="gallery" />
        )}

        {currentView === 'outro' && (
          <OutroScene 
            key="outro"
            onRestart={restartIntro}
          />
        )}
      </AnimatePresence>

      {/* Empty state for slideshow */}
      {currentView === 'slideshow' && galleryData.length === 0 && (
        <div className="fixed inset-0 bg-navy flex items-center justify-center">
          <div className="text-center">
            <h2 className="text-3xl font-light text-cream mb-6">Building your memories...</h2>
            <p className="text-cream/70 mb-8 max-w-md">
              Add photos and videos to the mariaimg folder, then run <code className="bg-navy/50 px-2 py-1 rounded">npm run build:gallery</code> to generate the gallery.
            </p>
            <motion.button
              onClick={() => setCurrentView('opening')}
              className="px-8 py-3 bg-gold/20 hover:bg-gold/30 text-cream border border-gold/40 rounded-2xl font-medium transition-all duration-300 hover:scale-105 focus:outline-none focus:ring-2 focus:ring-gold/50"
              whileHover={{ scale: 1.05 }}
              whileTap={{ scale: 0.95 }}
            >
              Back to Opening
            </motion.button>
          </div>
        </div>
      )}

      {/* Lightbox */}
      <Lightbox
        items={galleryData}
        initialIndex={lightboxIndex}
        isOpen={lightboxOpen}
        onClose={closeLightbox}
        onIndexChange={setLightboxIndex}
      />

      {/* Navigation toggle (hidden for now, can be enabled later) */}
      {/* {currentView === 'slideshow' && (
        <motion.button
          onClick={() => setCurrentView('gallery')}
          className="fixed top-6 left-6 p-3 bg-navy/80 hover:bg-navy/90 text-cream border border-gold/30 rounded-full transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-gold/50 z-10"
          initial={{ opacity: 0 }}
          animate={{ opacity: 1 }}
          transition={{ delay: 1 }}
          whileHover={{ scale: 1.1 }}
          whileTap={{ scale: 0.9 }}
        >
          <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
            <path d="M5 3a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2V5a2 2 0 00-2-2H5zM5 11a2 2 0 00-2 2v2a2 2 0 002 2h2a2 2 0 002-2v-2a2 2 0 00-2-2H5zM11 5a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V5zM11 13a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z" />
          </svg>
        </motion.button>
      )} */}
    </div>
  );
}
