import type { Metadata } from "next";
import { Geist, Geist_Mono } from "next/font/google";
import "./globals.css";

const geistSans = Geist({
  variable: "--font-geist-sans",
  subsets: ["latin"],
});

const geistMono = Geist_Mono({
  variable: "--font-geist-mono",
  subsets: ["latin"],
});

export const metadata: Metadata = {
  title: {
    default: "For Maria",
    template: "%s · For Maria",
  },
  description:
    "A cinematic slideshow of our memories — Happy Valentine's Day.",
  icons: {
    icon: "/favicon.svg",
    shortcut: "/favicon.svg",
  },
  themeColor: "#0B1220",
  openGraph: {
    title: "For Maria",
    description:
      "A cinematic slideshow of our memories — Happy Valentine's Day.",
    type: "website",
    siteName: "For Maria",
    images: [
      {
        url: "/opengraph-image",
        width: 1200,
        height: 630,
        alt: "For Maria — Happy Valentine's Day",
      },
    ],
  },
  twitter: {
    card: "summary_large_image",
    title: "For Maria",
    description:
      "A cinematic slideshow of our memories — Happy Valentine's Day.",
    images: [
      {
        url: "/twitter-image",
        alt: "For Maria — Happy Valentine's Day",
      },
    ],
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body
        className={`${geistSans.variable} ${geistMono.variable} antialiased`}
      >
        {children}
      </body>
    </html>
  );
}
