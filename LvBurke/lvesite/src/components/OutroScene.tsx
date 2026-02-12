'use client';

import { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';

interface OutroSceneProps {
  onRestart?: () => void;
}

const outroMessages = [
  "Thank you for always being there for me.",
  "Thank you for the memories"
];

export default function OutroScene({ onRestart }: OutroSceneProps) {
  const [currentMessage, setCurrentMessage] = useState(0);
  const [showControls, setShowControls] = useState(false);

  useEffect(() => {
    const timer = setTimeout(() => {
      if (currentMessage < outroMessages.length - 1) {
        setCurrentMessage(currentMessage + 1);
      } else {
        setTimeout(() => setShowControls(true), 3000);
      }
    }, currentMessage === 0 ? 5000 : 6000); // Longer pause for reading

    return () => clearTimeout(timer);
  }, [currentMessage]);

  useEffect(() => {
    const handleKeyPress = (event: KeyboardEvent) => {
      if (event.code === 'Space' || event.code === 'Enter') {
        event.preventDefault();
        if (onRestart) {
          onRestart();
        }
      }
    };

    if (showControls) {
      document.addEventListener('keydown', handleKeyPress);
      return () => document.removeEventListener('keydown', handleKeyPress);
    }
  }, [showControls, onRestart]);

  // Particle animation component with hearts
  const Particles = () => (
    <div className="absolute inset-0 overflow-hidden pointer-events-none">
      {Array.from({ length: 40 }).map((_, i) => (
        <motion.div
          key={i}
          className="absolute"
          initial={{
            x: Math.random() * (typeof window !== 'undefined' ? window.innerWidth : 1200),
            y: typeof window !== 'undefined' ? window.innerHeight + 50 : 800,
            opacity: 0,
          }}
          animate={{
            y: -100,
            opacity: [0, 0.9, 0],
            rotate: [0, 360],
          }}
          transition={{
            duration: Math.random() * 5 + 8,
            repeat: Infinity,
            delay: Math.random() * 10,
            ease: "easeOut",
          }}
        >
          {i % 3 === 0 ? (
            // Heart particle
            <svg className="w-4 h-4 text-gold/50" fill="currentColor" viewBox="0 0 20 20">
              <path fillRule="evenodd" d="M3.172 5.172a4 4 0 015.656 0L10 6.343l1.172-1.171a4 4 0 115.656 5.656L10 17.657l-6.828-6.829a4 4 0 010-5.656z" clipRule="evenodd" />
            </svg>
          ) : (
            // Regular particle
            <div className="w-1.5 h-1.5 bg-gold/40 rounded-full" />
          )}
        </motion.div>
      ))}
    </div>
  );

  return (
    <motion.div
      className="fixed inset-0 bg-gradient-to-br from-navy via-navy/95 to-navy/85 flex items-center justify-center"
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
      transition={{ duration: 2 }}
    >
      {/* Multiple gradient overlays for depth */}
      <div className="absolute inset-0 bg-gradient-radial from-transparent via-navy/10 to-navy/60" />
      <div className="absolute inset-0 bg-gradient-to-t from-navy/40 via-transparent to-navy/20" />
      
      {/* Soft glow effect */}
      <div className="absolute inset-0 bg-gradient-radial from-gold/8 via-transparent to-transparent" />
      
      {/* Particles */}
      <Particles />
      
      {/* Content */}
      <div className="relative z-10 max-w-5xl mx-auto px-8 text-center">
        {/* Messages */}
        <AnimatePresence mode="wait">
          <motion.h1
            key={currentMessage}
            className="text-4xl md:text-6xl lg:text-7xl xl:text-8xl font-light leading-relaxed mb-12 md:mb-16 lg:mb-20 max-w-6xl mx-auto tracking-wide text-cream"
            initial={{ opacity: 0, y: 50, scale: 0.8 }}
            animate={{ opacity: 1, y: 0, scale: 1 }}
            exit={{ opacity: 0, y: -50, scale: 1.2 }}
            transition={{ 
              duration: 1.5, 
              ease: "easeOut",
              scale: { duration: 2 }
            }}
            style={{
              textShadow: '0 4px 20px rgba(0, 0, 0, 0.3), 0 8px 40px rgba(231, 200, 136, 0.2)',
              lineHeight: '1.3',
            }}
          >
            {outroMessages[currentMessage]}
          </motion.h1>
        </AnimatePresence>

        {/* Controls */}
        <AnimatePresence>
          {showControls && (
            <motion.div
              className="space-y-8 mt-12"
              initial={{ opacity: 0, y: 40 }}
              animate={{ opacity: 1, y: 0 }}
              transition={{ duration: 1.5, delay: 0.8 }}
            >
              {onRestart && (
                <motion.button
                  onClick={onRestart}
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
                  <span className="relative z-10 tracking-wider">Experience Again</span>
                  <motion.div
                    className="absolute inset-0 bg-gradient-to-r from-gold/20 to-gold/30 rounded-3xl opacity-0"
                    whileHover={{ opacity: 1 }}
                    transition={{ duration: 0.3 }}
                  />
                </motion.button>
              )}
              
              <motion.p
                className="text-cream/70 text-base md:text-lg tracking-wide"
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                transition={{ delay: 1.5, duration: 0.8 }}
                style={{
                  textShadow: '0 2px 8px rgba(0, 0, 0, 0.6)',
                }}
              >
                Press <kbd className="px-2 py-1 bg-cream/10 rounded border border-cream/20 text-gold font-mono text-sm">Space</kbd> to begin again
              </motion.p>
            </motion.div>
          )}
        </AnimatePresence>
      </div>
    </motion.div>
  );
}
