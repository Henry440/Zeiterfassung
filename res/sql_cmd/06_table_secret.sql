CREATE TABLE "secrets" (
	"id"	INTEGER,
	"user_id"	INTEGER NOT NULL,
	"secret"	TEXT NOT NULL,
	"inizialised"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
)