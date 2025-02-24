CREATE TABLE Users (
    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    role TEXT CHECK (
        role IN ('Director', 'Coach', 'Artist')
    ) NOT NULL,
    hashed_password TEXT NOT NULL
);

CREATE TABLE Training_Sessions (
    session_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    duration INTEGER NOT NULL, -- Duration in minutes
    performance_notes TEXT,
    FOREIGN KEY (user_id) REFERENCES Users (user_id) ON DELETE CASCADE
);

CREATE TABLE Attendance (
    attendance_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    session_id INTEGER NOT NULL,
    status TEXT CHECK (
        status IN ('Present', 'Absent')
    ) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users (user_id) ON DELETE CASCADE,
    FOREIGN KEY (session_id) REFERENCES Training_Sessions (session_id) ON DELETE CASCADE
);

CREATE TABLE Injury_Records (
    injury_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    date TEXT NOT NULL,
    description TEXT NOT NULL,
    recovery_status TEXT CHECK (
        recovery_status IN (
            'New',
            'Recovering',
            'Cleared'
        )
    ) NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users (user_id) ON DELETE CASCADE
);