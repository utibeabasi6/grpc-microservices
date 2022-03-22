CREATE TABLE IF NOT EXISTS products(name VARCHAR(255), price INTEGER, image VARCHAR(255));
 
INSERT INTO products VALUES('Nike', '200', 'https://images.unsplash.com/photo-1542291026-7eec264c27ff?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxzZWFyY2h8MXx8c2hvZXxlbnwwfHwwfHw%3D&w=1000&q=80');
INSERT INTO products VALUES('Adidas', 500, 'https://media.istockphoto.com/photos/sport-shoes-on-isolated-white-background-picture-id956501428?k=20&m=956501428&s=612x612&w=0&h=UC4qdZa2iA0PJvv0RIBlJDyF80wxFyLPq4YWvZa30Sc=');
INSERT INTO products VALUES('Chuka', 1500, 'https://media.istockphoto.com/photos/brown-leather-shoe-picture-id187310279?k=20&m=187310279&s=612x612&w=0&h=WDavpCxsLbj_PRpoY-3PsS2zvuP0Vk0Ci22sRLO9DzE=');

CREATE TABLE IF NOT EXISTS videos(url VARCHAR(255));
INSERT INTO videos VALUES ('https://www.youtube.com/watch?v=uHKfrz65KSU');
