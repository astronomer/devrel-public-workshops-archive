INSERT INTO bookings (customer_id, route_id, booked_at, departure_date, return_date, passengers, promo_code) VALUES
(1002, 1001, '2025-11-10 08:30:00', '2025-12-01', '2025-12-04', 1, NULL),
(1004, 1002, '2025-11-20 09:15:00', '2026-02-15', '2026-08-15', 2, NULL),
(1003, 1003, '2025-12-15 16:30:00', '2026-07-01', '2027-01-01', 3, NULL);

INSERT INTO payments (booking_id, paid_at, amount_usd) VALUES
(5, '2025-11-10 08:45:00', 4000),
(6, '2025-11-20 09:30:00', 60000),
(7, '2025-12-15 16:45:00', 180000);

INSERT INTO trip_reviews (review_id, booking_id, review_text, image_path, submitted_at) VALUES
-- Safety concerns (Moon landings)
(1, 1, 'The landing on the Moon was terrifying. Severe turbulence during descent and the pilot seemed to struggle with the approach. My children were scared and crying. This needs to be addressed before someone gets hurt.', 'images/review_1.jpg', '2025-10-20 14:30:00'),
(2, 5, 'Rough landing experience on the Moon. The final approach was extremely bumpy and several passengers felt unwell afterward. The crew handled the situation professionally but the experience was genuinely frightening. Is this normal?', NULL, '2025-12-06 09:15:00'),

-- Positive experiences (destinations)
(3, 4, 'Europa exceeded all expectations! The ice formations are breathtaking and the guided tour of the subsurface ocean viewing station was a once-in-a-lifetime experience. The crew went above and beyond. Worth every penny of the $96,000 we paid.', 'images/review_3.jpg', '2025-12-30 11:00:00'),
(4, 2, 'Mars at sunset is something everyone should experience at least once. The red dunes stretching to the horizon, the thin atmosphere making stars visible even during twilight. Our guide was incredibly knowledgeable about the geology. Magical trip.', NULL, '2026-01-15 20:30:00'),

-- Value/pricing complaints
(5, 6, 'I paid $60,000 for two passengers to Mars and the onboard food was terrible. Vacuum-sealed packets for every meal at this price point? I expected fresh-prepared meals and a proper dining experience. Very disappointed with the value proposition.', 'images/review_5.jpg', '2026-03-01 17:20:00'),
(6, 4, 'I used the ASTRO20 promo code which should give 20 percent off but looking at my receipt the math does not add up. We were charged $96,000 for 2 passengers to Europa. Can someone please review my billing? I believe I was overcharged.', NULL, '2026-01-02 10:45:00'),

-- Service quality (crew and communication)
(7, 7, 'The crew on our Europa journey was exceptional - always attentive and knowledgeable about the geology. However, the entertainment system was outdated and kept glitching, and the sleep pods were uncomfortably cramped for a 6-month journey.', NULL, '2026-08-01 22:15:00'),
(8, 3, 'Booking process was smooth and the pre-flight briefing was thorough and informative. However, communication during the actual Moon trip was severely lacking. We did not receive updates about schedule changes and missed a planned surface excursion because of it.', NULL, '2026-01-15 11:00:00');
