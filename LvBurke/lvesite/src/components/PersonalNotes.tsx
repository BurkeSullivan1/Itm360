'use client';

import { motion, AnimatePresence } from 'framer-motion';

interface PersonalNotesProps {
  currentIndex: number;
  totalItems: number;
}

// Your personal words for each photo/moment
const personalWords = [
  "This moment still makes me smile every time I see it",
  "Thank you for meeting my mom that day",
  "This was a fun day minus the sunburn",
  "I wish I could go back to this moment",
  "I loved watching you be at peace",
  "I dont know how I got so lucky to have you",
  "I'll always be there to carry you",
  "okay i just threw this one in here",
  "You were my wonder woman",
  "I miss these moments the most with you",
  "I will always miss your laugh and personality",
  "This is exactly how I want to remember us",
  "Okay you look really good here",
  "Im happy I met you",
  "Thank you for this day and i was happy to celebrate you",
  "I remember we just wanted to take more photos togeather",
  "You looked so beautiful and carefree here",
  "This was my first photo on my phone of you",
  "I was happy you brought me there that day",
  "This is you in your element",
  "I can still feel how happy we were here",
  "Ok enough with the jetskis",
  "im happy I got to spend so much time with you",
  "I treasure every second we spent together"
];

export default function PersonalNotes({ currentIndex, totalItems }: PersonalNotesProps) {
  const currentWords = personalWords[currentIndex % personalWords.length];

  return (
    <motion.div
      className="fixed left-8 top-1/2 transform -translate-y-1/2 max-w-md w-full z-20"
      initial={{ opacity: 0, x: -80 }}
      animate={{ opacity: 1, x: 0 }}
      transition={{ duration: 1, delay: 1.2 }}
    >
      <AnimatePresence mode="wait">
        <motion.div
          key={currentIndex}
          className="relative bg-gradient-to-br from-navy/95 to-navy/85 backdrop-blur-lg border-2 border-gold/30 rounded-3xl p-8 shadow-2xl"
          initial={{ opacity: 0, x: -40, scale: 0.9, rotateY: -10 }}
          animate={{ opacity: 1, x: 0, scale: 1, rotateY: 0 }}
          exit={{ opacity: 0, x: 40, scale: 0.9, rotateY: 10 }}
          transition={{ duration: 0.8, ease: "easeOut" }}
          style={{
            boxShadow: '0 25px 50px rgba(0, 0, 0, 0.4), inset 0 1px 0 rgba(231, 200, 136, 0.2)'
          }}
        >
          {/* Decorative corner elements */}
          <div className="absolute top-3 left-3 w-6 h-6 border-l-2 border-t-2 border-gold/40 rounded-tl-lg" />
          <div className="absolute top-3 right-3 w-6 h-6 border-r-2 border-t-2 border-gold/40 rounded-tr-lg" />
          <div className="absolute bottom-3 left-3 w-6 h-6 border-l-2 border-b-2 border-gold/40 rounded-bl-lg" />
          <div className="absolute bottom-3 right-3 w-6 h-6 border-r-2 border-b-2 border-gold/40 rounded-br-lg" />
          
          {/* Header with enhanced design */}
          <motion.div
            className="flex items-center justify-center mb-6"
            initial={{ opacity: 0, scale: 0.8 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 0.4, duration: 0.6 }}
          >
            <div className="flex items-center space-x-3">
              <motion.svg 
                className="w-7 h-7 text-gold" 
                fill="currentColor" 
                viewBox="0 0 20 20"
                animate={{ 
                  scale: [1, 1.1, 1],
                  rotate: [0, 5, -5, 0]
                }}
                transition={{ 
                  duration: 3,
                  repeat: Infinity,
                  ease: "easeInOut"
                }}
              >
                <path fillRule="evenodd" d="M3.172 5.172a4 4 0 015.656 0L10 6.343l1.172-1.171a4 4 0 115.656 5.656L10 17.657l-6.828-6.829a4 4 0 010-5.656z" clipRule="evenodd" />
              </motion.svg>
              <div className="text-center">
                <span className="text-gold text-lg font-semibold tracking-wide">My Thoughts</span>
                <div className="w-full h-0.5 bg-gradient-to-r from-transparent via-gold/60 to-transparent mt-1" />
              </div>
              <motion.svg 
                className="w-7 h-7 text-gold" 
                fill="currentColor" 
                viewBox="0 0 20 20"
                animate={{ 
                  scale: [1, 1.1, 1],
                  rotate: [0, -5, 5, 0]
                }}
                transition={{ 
                  duration: 3,
                  repeat: Infinity,
                  ease: "easeInOut",
                  delay: 1.5
                }}
              >
                <path fillRule="evenodd" d="M3.172 5.172a4 4 0 015.656 0L10 6.343l1.172-1.171a4 4 0 115.656 5.656L10 17.657l-6.828-6.829a4 4 0 010-5.656z" clipRule="evenodd" />
              </motion.svg>
            </div>
          </motion.div>
          
          {/* Message content with enhanced typography */}
          <motion.div
            className="text-center mb-6"
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.6, duration: 0.8 }}
          >
            <p className="text-cream text-lg leading-relaxed font-light tracking-wide italic px-2"
               style={{
                 textShadow: '0 2px 4px rgba(0, 0, 0, 0.3)',
                 lineHeight: '1.6'
               }}>
              &ldquo;{currentWords}&rdquo;
            </p>
          </motion.div>
          
          {/* Enhanced footer with memory count */}
          <motion.div
            className="flex items-center justify-between pt-6 border-t border-gold/20"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            transition={{ delay: 0.8, duration: 0.6 }}
          >
            <div className="flex items-center space-x-2">
              <div className="w-2 h-2 bg-gold/60 rounded-full animate-pulse" />
              <span className="text-cream/80 text-sm font-medium">
                Memory {currentIndex + 1}
              </span>
            </div>
            
            <div className="text-cream/60 text-sm">
              of {totalItems}
            </div>
          </motion.div>
          
          {/* Subtle floating particles */}
          <div className="absolute inset-0 overflow-hidden pointer-events-none rounded-3xl">
            {Array.from({ length: 6 }).map((_, i) => (
              <motion.div
                key={i}
                className="absolute w-1 h-1 bg-gold/30 rounded-full"
                initial={{
                  x: Math.random() * 300,
                  y: Math.random() * 200,
                  opacity: 0,
                }}
                animate={{
                  y: [null, -20, -40],
                  opacity: [0, 0.6, 0],
                }}
                transition={{
                  duration: 4 + Math.random() * 2,
                  repeat: Infinity,
                  delay: Math.random() * 3,
                  ease: "easeOut",
                }}
              />
            ))}
          </div>
        </motion.div>
      </AnimatePresence>
    </motion.div>
  );
}
