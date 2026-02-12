'use client';

import { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import Image from 'next/image';
import { MediaItem } from '@/lib/gallery';

interface LightboxProps {
  items: MediaItem[];
  initialIndex: number;
  isOpen: boolean;
  onClose: () => void;
  onIndexChange?: (index: number) => void;
}

export default function Lightbox({
  items,
  initialIndex,
  isOpen,
  onClose,
  onIndexChange,
}: LightboxProps) {
  const [currentIndex, setCurrentIndex] = useState(initialIndex);

  const currentItem = items[currentIndex];

  useEffect(() => {
    setCurrentIndex(initialIndex);
  }, [initialIndex]);

  useEffect(() => {
    onIndexChange?.(currentIndex);
  }, [currentIndex, onIndexChange]);

  useEffect(() => {
    const handleKeyPress = (event: KeyboardEvent) => {
      if (!isOpen) return;

      switch (event.code) {
        case 'Escape':
          onClose();
          break;
        case 'ArrowLeft':
          event.preventDefault();
          setCurrentIndex(prev => prev === 0 ? items.length - 1 : prev - 1);
          break;
        case 'ArrowRight':
          event.preventDefault();
          setCurrentIndex(prev => prev === items.length - 1 ? 0 : prev + 1);
          break;
      }
    };

    if (isOpen) {
      document.addEventListener('keydown', handleKeyPress);
      // Prevent body scroll
      document.body.style.overflow = 'hidden';
    }

    return () => {
      document.removeEventListener('keydown', handleKeyPress);
      document.body.style.overflow = 'unset';
    };
  }, [isOpen, items.length, onClose]);

  if (!isOpen || !currentItem) return null;

  return (
    <AnimatePresence>
      <motion.div
        className="fixed inset-0 bg-navy/95 backdrop-blur-sm z-50 flex items-center justify-center"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        exit={{ opacity: 0 }}
        transition={{ duration: 0.3 }}
        onClick={onClose}
      >
        {/* Close button */}
        <motion.button
          onClick={onClose}
          className="absolute top-6 right-6 p-3 bg-navy/80 hover:bg-navy/90 text-cream border border-gold/30 rounded-full transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-gold/50 z-10"
          initial={{ opacity: 0, scale: 0.8 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ delay: 0.2 }}
          whileHover={{ scale: 1.1 }}
          whileTap={{ scale: 0.9 }}
        >
          <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 20 20">
            <path fillRule="evenodd" d="M4.293 4.293a1 1 0 011.414 0L10 8.586l4.293-4.293a1 1 0 111.414 1.414L11.414 10l4.293 4.293a1 1 0 01-1.414 1.414L10 11.414l-4.293 4.293a1 1 0 01-1.414-1.414L8.586 10 4.293 5.707a1 1 0 010-1.414z" clipRule="evenodd" />
          </svg>
        </motion.button>

        {/* Navigation buttons */}
        {items.length > 1 && (
          <>
            {/* Previous button */}
            <motion.button
              onClick={(e) => {
                e.stopPropagation();
                setCurrentIndex(prev => prev === 0 ? items.length - 1 : prev - 1);
              }}
              className="absolute left-6 top-1/2 transform -translate-y-1/2 p-4 bg-navy/80 hover:bg-navy/90 text-cream border border-gold/30 rounded-full transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-gold/50 z-10"
              initial={{ opacity: 0, x: -20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: 0.3 }}
              whileHover={{ scale: 1.1 }}
              whileTap={{ scale: 0.9 }}
            >
              <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 20 20">
                <path fillRule="evenodd" d="M12.707 5.293a1 1 0 010 1.414L9.414 10l3.293 3.293a1 1 0 01-1.414 1.414l-4-4a1 1 0 010-1.414l4-4a1 1 0 011.414 0z" clipRule="evenodd" />
              </svg>
            </motion.button>

            {/* Next button */}
            <motion.button
              onClick={(e) => {
                e.stopPropagation();
                setCurrentIndex(prev => prev === items.length - 1 ? 0 : prev + 1);
              }}
              className="absolute right-6 top-1/2 transform -translate-y-1/2 p-4 bg-navy/80 hover:bg-navy/90 text-cream border border-gold/30 rounded-full transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-gold/50 z-10"
              initial={{ opacity: 0, x: 20 }}
              animate={{ opacity: 1, x: 0 }}
              transition={{ delay: 0.3 }}
              whileHover={{ scale: 1.1 }}
              whileTap={{ scale: 0.9 }}
            >
              <svg className="w-6 h-6" fill="currentColor" viewBox="0 0 20 20">
                <path fillRule="evenodd" d="M7.293 14.707a1 1 0 010-1.414L10.586 10 7.293 6.707a1 1 0 011.414-1.414l4 4a1 1 0 010 1.414l-4 4a1 1 0 01-1.414 0z" clipRule="evenodd" />
              </svg>
            </motion.button>
          </>
        )}

        {/* Media content */}
        <motion.div
          className="relative max-w-[90vw] max-h-[90vh] flex items-center justify-center"
          initial={{ opacity: 0, scale: 0.8 }}
          animate={{ opacity: 1, scale: 1 }}
          transition={{ duration: 0.4, ease: "easeOut" }}
          onClick={(e) => e.stopPropagation()}
        >
          <AnimatePresence mode="wait">
            <motion.div
              key={currentIndex}
              initial={{ opacity: 0, scale: 1.1 }}
              animate={{ opacity: 1, scale: 1 }}
              exit={{ opacity: 0, scale: 0.9 }}
              transition={{ duration: 0.3 }}
              className="relative"
            >
              {currentItem.type === 'image' ? (
                <Image
                  src={currentItem.src}
                  alt={currentItem.caption || `Memory ${currentIndex + 1}`}
                  width={currentItem.width || 800}
                  height={currentItem.height || 600}
                  className="max-w-full max-h-[80vh] object-contain rounded-lg shadow-2xl"
                  priority
                  quality={95}
                />
              ) : (
                <video
                  src={currentItem.src}
                  className="max-w-full max-h-[80vh] object-contain rounded-lg shadow-2xl"
                  controls
                  autoPlay
                  muted
                  playsInline
                />
              )}
            </motion.div>
          </AnimatePresence>
        </motion.div>

        {/* Caption */}
        <AnimatePresence>
          {currentItem.caption && (
            <motion.div
              key={currentItem.caption}
              className="absolute bottom-8 left-8 right-8 text-center"
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: 20 }}
              transition={{ duration: 0.4 }}
            >
              <p className="text-cream text-lg font-light leading-relaxed max-w-4xl mx-auto bg-navy/60 backdrop-blur-sm rounded-2xl px-6 py-3 border border-gold/20">
                {currentItem.caption}
              </p>
            </motion.div>
          )}
        </AnimatePresence>

        {/* Counter */}
        <motion.div
          className="absolute top-6 left-6 text-cream/80 text-sm font-medium bg-navy/60 backdrop-blur-sm rounded-full px-4 py-2 border border-gold/20"
          initial={{ opacity: 0, y: -20 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.4 }}
        >
          {currentIndex + 1} of {items.length}
        </motion.div>
      </motion.div>
    </AnimatePresence>
  );
}
