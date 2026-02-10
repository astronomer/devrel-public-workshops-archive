CREATE TABLE IF NOT EXISTS trip_reviews (
    review_id       INTEGER PRIMARY KEY,
    booking_id      INTEGER NOT NULL REFERENCES bookings(booking_id),
    review_text     TEXT NOT NULL,
    image_path      VARCHAR,
    submitted_at    TIMESTAMP NOT NULL,
    status          VARCHAR DEFAULT 'pending',
    sentiment       VARCHAR,
    category        VARCHAR,
    summary         VARCHAR,
    image_analysis  VARCHAR,
    routed_to       VARCHAR,
    ai_response     TEXT,
    approved_at     TIMESTAMP
);

CREATE TABLE IF NOT EXISTS review_embeddings (
    review_id   INTEGER PRIMARY KEY REFERENCES trip_reviews(review_id),
    embedding   DOUBLE[] NOT NULL,
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
