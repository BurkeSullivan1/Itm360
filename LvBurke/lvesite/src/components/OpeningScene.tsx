'use client';

import { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';

interface OpeningSceneProps {
  onStart: () => void;
  onToggleSound: () => void;
  isSoundEnabled: boolean;
}

const messages = [
  "For Maria",
  "Happy Valentine's Day",
  "This is for you"
];

export default function OpeningScene({ onStart, onToggleSound, isSoundEnabled }: OpeningSceneProps) {
  const [currentMessage, setCurrentMessage] = useState(0);
  const [showCTA, setShowCTA] = useState(false);

  useEffect(() => {
    const timer = setTimeout(() => {
      if (currentMessage < messages.length - 1) {
        setCurrentMessage(currentMessage + 1);
      } else {
        setTimeout(() => setShowCTA(true), 2000);
      }
    }, currentMessage === 0 ? 4000 : 5000); // Longer pause for first message, then more time for reading

    return () => clearTimeout(timer);
  }, [currentMessage]);

  useEffect(() => {
    const handleKeyPress = (event: KeyboardEvent) => {
      if (event.code === 'Space' || event.code === 'Enter') {
        event.preventDefault();
        onStart();
      }
    };

    if (showCTA) {
      document.addEventListener('keydown', handleKeyPress);
      return () => document.removeEventListener('keydown', handleKeyPress);
    }
  }, [showCTA, onStart]);

  // Hearts balloon animation for Valentine's message
  const HeartsBalloon = () => {
    const reduceMotion = typeof window !== 'undefined' && window.matchMedia('(prefers-reduced-motion: reduce)').matches;

    return (
      <div className="absolute inset-0 overflow-hidden pointer-events-none">
        {Array.from({ length: reduceMotion ? 12 : 28 }).map((_, i) => {
          const startX = Math.random() * (typeof window !== 'undefined' ? window.innerWidth : 1200);
          const startY = (typeof window !== 'undefined' ? window.innerHeight : 800) + 60 + Math.random() * 60;
          const drift = (Math.random() * 80 + 40) * (Math.random() < 0.5 ? -1 : 1);
          const size = Math.random() * 24 + 16; // 16px - 40px
          const duration = (Math.random() * 3 + 7) * (reduceMotion ? 0.7 : 1);
          const delay = Math.random() * 4;

          return (
            <motion.div
              key={i}
              className="absolute"
              initial={{
                x: startX,
                y: startY,
                opacity: 0,
                scale: 0.9,
              }}
              animate={{
                y: reduceMotion ? startY - 120 : -120,
                x: [startX, startX + drift, startX - drift * 0.5],
                opacity: [0, 0.9, 0.2, 0],
                rotate: [0, 6, -4, 0],
                scale: reduceMotion ? 1 : [0.95, 1.05, 1],
              }}
              transition={{
                duration,
                repeat: Infinity,
                delay,
                ease: "easeOut",
              }}
            >
              <svg
                className="text-gold/60 drop-shadow"
                style={{ width: size, height: size }}
                fill="currentColor"
                viewBox="0 0 20 20"
                aria-hidden="true"
              >
                <path fillRule="evenodd" d="M3.172 5.172a4 4 0 015.656 0L10 6.343l1.172-1.171a4 4 0 115.656 5.656L10 17.657l-6.828-6.829a4 4 0 010-5.656z" clipRule="evenodd" />
              </svg>
            </motion.div>
          );
        })}
      </div>
    );
  };

  return (
    <motion.div
      className="fixed inset-0 bg-gradient-to-br from-navy via-navy/95 to-navy/90 flex items-center justify-center"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      transition={{ duration: 1.5 }}
    >
      {/* Multiple vignette overlays for depth */}
      <div className="absolute inset-0 bg-gradient-radial from-transparent via-navy/10 to-navy/70" />
      <div className="absolute inset-0 bg-gradient-to-t from-navy/50 via-transparent to-navy/30" />
      
      {/* Soft glow effect */}
      <div className="absolute inset-0 bg-gradient-radial from-gold/5 via-transparent to-transparent" />
      
      {/* Hearts balloon animation only during Valentine's message */}
      {currentMessage === 1 && <HeartsBalloon />}
      
      {/* Content */}
      <div className="relative z-10 max-w-5xl mx-auto px-8 text-center">
        {/* Messages */}
        <AnimatePresence mode="wait">
          <motion.h1
            key={currentMessage}
            className={`font-light leading-relaxed mb-12 md:mb-16 lg:mb-20 max-w-5xl mx-auto tracking-wide ${
              currentMessage === 0 
                ? 'text-5xl md:text-7xl lg:text-8xl xl:text-9xl text-gold drop-shadow-2xl' // "For Maria" - larger and gold
                : 'text-3xl md:text-5xl lg:text-6xl xl:text-7xl text-cream'
            }`}
            initial={{ opacity: 0, y: 40, scale: 0.9 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            exit={{ opacity: 0, y: -40, scale: 1.1 }}
            transition={{ 
              duration: 1.2, 
              ease: "easeOut",
              scale: { duration: 1.5 }
            }}
            style={{
              textShadow: currentMessage === 0 
                ? '0 8px 32px rgba(231, 200, 136, 0.4), 0 4px 20px rgba(0, 0, 0, 0.3)'
                : '0 4px 20px rgba(0, 0, 0, 0.3)',
              lineHeight: '1.4',
            }}
          >
            {messages[currentMessage]}
          </motion.h1>
        </AnimatePresence>

        {/* CTA Button */}
        <AnimatePresence>
          {showCTA && (
            <motion.div
              className="space-y-8 mt-8"
              initial={{ opacity: 0, y: 40 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 1.2, delay: 0.6 }}
            >
              <motion.button
                onClick={onStart}
                className="group relative px-16 py-5 bg-gradient-to-r from-gold/20 to-gold/30 hover:from-gold/30 hover:to-gold/40 text-cream border-2 border-gold/50 hover:border-gold/70 rounded-3xl font-medium text-xl transition-all duration-500 hover:scale-110 focus:outline-none focus:ring-4 focus:ring-gold/30 shadow-2xl"
                whileHover={{ 
                  scale: 1.1,
                  boxShadow: "0 20px 40px rgba(231, 200, 136, 0.3)"
                }}
                whileTap={{ scale: 0.95 }}
                style={{
                  backdropFilter: 'blur(10px)',
                  textShadow: '0 2px 10px rgba(0, 0, 0, 0.5)',
                }}
              >
                <span className="relative z-10 tracking-wider">Play Memories</span>
                <motion.div
                  className="absolute inset-0 bg-gradient-to-r from-gold/20 to-gold/30 rounded-3xl opacity-0"
                  whileHover={{ opacity: 1 }}
                  transition={{ duration: 0.3 }}
                />
              </motion.button>
              
              <motion.p
                className="text-cream/70 text-base md:text-lg tracking-wide"
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ delay: 1.2, duration: 0.8 }}
                style={{
                  textShadow: '0 2px 8px rgba(0, 0, 0, 0.6)',
                }}
              >
                Press <kbd className="px-2 py-1 bg-cream/10 rounded border border-cream/20 text-gold font-mono text-sm">Space</kbd> or <kbd className="px-2 py-1 bg-cream/10 rounded border border-cream/20 text-gold font-mono text-sm">Enter</kbd> to begin your journey
              </motion.p>
            </motion.div>
          )}
        </AnimatePresence>

        {/* Sound toggle */}
        <motion.button
          onClick={onToggleSound}
          className="fixed bottom-8 right-8 p-3 bg-navy/50 hover:bg-navy/70 text-cream border border-gold/30 rounded-full transition-all duration-300 focus:outline-none focus:ring-2 focus:ring-gold/50"
          initial={{ opacity: 0 }}
          animate={{ opacity: showCTA ? 1 : 0 }}
          whileHover={{ scale: 1.1 }}
          whileTap={{ scale: 0.9 }}
        >
          {isSoundEnabled ? (
            <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
              <path fillRule="evenodd" d="M9.383 3.076A1 1 0 0110 4v12a1 1 0 01-1.617.795L4.09 13H2a1 1 0 01-1-1V8a1 1 0 011-1h2.09l4.293-3.795A1 1 0 019.383 3.076zM12.293 7.293a1 1 0 011.414 0L15 8.586l1.293-1.293a1 1 0 111.414 1.414L16.414 10l1.293 1.293a1 1 0 01-1.414 1.414L15 11.414l-1.293 1.293a1 1 0 01-1.414-1.414L13.586 10l-1.293-1.293a1 1 0 010-1.414z" clipRule="evenodd" />
            </svg>
          ) : (
            <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
              <path fillRule="evenodd" d="M9.383 3.076A1 1 0 0110 4v12a1 1 0 01-1.617.795L4.09 13H2a1 1 0 01-1-1V8a1 1 0 011-1h2.09l4.293-3.795A1 1 0 019.383 3.076zM14.657 2.929a1 1 0 011.414 0A9.972 9.972 0 0119 10a9.972 9.972 0 01-2.929 7.071 1 1 0 01-1.414-1.414A7.971 7.971 0 0017 10c0-2.21-.894-4.208-2.343-5.657a1 1 0 010-1.414zm-2.829 2.828a1 1 0 011.415 0A5.983 5.983 0 0115 10a5.984 5.984 0 01-1.757 4.243 1 1 0 01-1.415-1.414A3.984 3.984 0 0013 10a3.983 3.983 0 00-1.172-2.828 1 1 0 010-1.415z" clipRule="evenodd" />
            </svg>
          )}
        </motion.button>
      </div>
    </motion.div>
  );
}
