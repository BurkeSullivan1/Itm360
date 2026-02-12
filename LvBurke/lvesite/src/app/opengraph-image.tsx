import { ImageResponse } from "next/og";

export const size = {
  width: 1200,
  height: 630,
};

export const contentType = "image/png";

export const runtime = "edge";

export default function OpengraphImage() {
  return new ImageResponse(
    (
      <div
        style={{
          width: size.width,
          height: size.height,
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          background: "linear-gradient(135deg, #0B1220 0%, #0B1220 60%, #0B1220 100%)",
          position: "relative",
          fontFamily: "system-ui, Segoe UI, Arial",
        }}
      >
        {/* Soft vignette */}
        <div
          style={{
            position: "absolute",
            inset: 0,
            background:
              "radial-gradient(closest-side, rgba(231,200,136,0.10), transparent 60%)",
          }}
        />

        {/* Heart icon */}
        <svg
          xmlns="http://www.w3.org/2000/svg"
          viewBox="0 0 20 20"
          width={140}
          height={140}
          style={{ marginRight: 36, filter: "drop-shadow(0 8px 28px rgba(231,200,136,0.35))" }}
          fill="#E7C888"
        >
          <path d="M3.172 5.172a4 4 0 015.656 0L10 6.343l1.172-1.171a4 4 0 115.656 5.656L10 17.657l-6.828-6.829a4 4 0 010-5.656z" />
        </svg>

        <div style={{ display: "flex", flexDirection: "column" }}>
          <div
            style={{
              color: "#E7C888",
              fontSize: 86,
              fontWeight: 300,
              letterSpacing: 2,
              textShadow: "0 6px 24px rgba(231,200,136,0.35)",
            }}
          >
            For Maria
          </div>
          <div
            style={{
              color: "#F7F5EF",
              fontSize: 36,
              marginTop: 10,
              opacity: 0.9,
            }}
          >
            Happy Valentine's Day · A cinematic slideshow of our memories
          </div>
        </div>
      </div>
    ),
    size
  );
}