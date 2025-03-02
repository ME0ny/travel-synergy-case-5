CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    telegram_id VARCHAR(255) UNIQUE NOT NULL,
    username VARCHAR(255)
);

CREATE TABLE IF NOT EXISTS entries (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    location_latitude FLOAT NOT NULL,
    location_longitude FLOAT NOT NULL,
    location_address VARCHAR(255),
    image_url VARCHAR(255) NOT NULL,
    category VARCHAR(50) CHECK (category IN ('CulturalHeritage', 'PlaceToVisit')),
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);