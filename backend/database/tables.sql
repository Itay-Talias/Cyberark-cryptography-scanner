CREATE DATABASE cryptography_scanner;
use cryptography_scanner;

CREATE TABLE organizations(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(128)
);

CREATE TABLE repositories(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(128),
    organization_id INT,
    FOREIGN KEY (organization_id) REFERENCES organizations(id)
);
CREATE TABLE files(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(128),
    url VARCHAR(50),
    repo_id INT,
    FOREIGN KEY (repo_id) REFERENCES repositories(id)
);
CREATE TABLE languages(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(128)
);
CREATE TABLE categories(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(128)
);
CREATE TABLE libraries(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(128),
    language_id INT,
    category_id INT,
    FOREIGN KEY (language_id) REFERENCES languages(id),
    FOREIGN KEY (category_id) REFERENCES categories(id)
);

CREATE TABLE libraries_files(
    file_id INT NOT NULL,
    library_id INT NOT NULL,
    PRIMARY KEY(file_id, library_id),
    FOREIGN KEY (file_id) REFERENCES files(id),
    FOREIGN KEY (library_id) REFERENCES libraries(id)
);
CREATE TABLE words(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    word VARCHAR(128)
);
CREATE TABLE libraries_words(
    library_id INT NOT NULL,
    word_id INT NOT NULL,
    PRIMARY KEY(library_id, word_id),
    FOREIGN KEY (library_id) REFERENCES libraries(id),
    FOREIGN KEY (word_id) REFERENCES words(id)
);

CREATE TABLE search_results(
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    file_id INT,
    line INT,
    library_id INT,
    word_id INT,
    FOREIGN KEY (file_id) REFERENCES files(id),
    FOREIGN KEY (library_id) REFERENCES libraries(id),
    FOREIGN KEY (word_id) REFERENCES words(id)
);
