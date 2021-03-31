INSERT INTO abteilung (name) VALUES ('Default');
INSERT INTO team (name, abteilung_id) VALUES ('Default', 1);
INSERT INTO user (name, team_id, stunden) VALUES ('Default', 1, 40); 

INSERT INTO aktion (name, beschreibung) VALUES ('Kommen','Betreten des Firmengebäudes, Beginn der Arbeitszeit');
INSERT INTO aktion (name, beschreibung) VALUES ('Gehen','Verlassen des Firmengebäudes, Ende der Arbeitszeit');
INSERT INTO aktion (name, beschreibung) VALUES ('Pause beginn','Pausiert die Arbeitszeit');
INSERT INTO aktion (name, beschreibung) VALUES ('Pause ende','Setzt die Arbeitszeit fort');
INSERT INTO aktion (name, beschreibung) VALUES ('Betr. Unterwegs beginn','');
INSERT INTO aktion (name, beschreibung) VALUES ('Betr. Unterwegs ende','');