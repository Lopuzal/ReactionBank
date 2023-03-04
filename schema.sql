DROP TABLE IF EXISTS Images;
DROP TABLE IF EXISTS Tags;
DROP TABLE IF EXISTS Folders;

CREATE TABLE Images (
id INTEGER PRIMARY KEY AUTOINCREMENT,
filePath TEXT,
idFolder INTEGER,
uploadDate TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
FOREIGN KEY(idFolder) REFERENCES Folders(id)
);

CREATE TABLE Tags (
tag TEXT,
idImage INTEGER,
PRIMARY KEY(tag, idImage)
FOREIGN KEY(idImage) REFERENCES Images(id)
);

CREATE TABLE Folders (
id INTEGER PRIMARY KEY AUTOINCREMENT,
folderPath TEXT
);

INSERT INTO Folders (folderPath) VALUES ("C:/Users/Lopuzal/Code/Reaction_bank");
INSERT INTO Images (filePath,idFolder) VALUES ("aoeaoeoae", 1),("sociss", 1);
INSERT INTO Tags (tag,idImage) VALUES ("oui",1),("non",1),("oui",2),("peut-etre",2);
