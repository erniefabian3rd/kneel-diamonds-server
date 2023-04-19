CREATE TABLE `Metal`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `metal` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Size`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `carets` INTEGER NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Style`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `style` NVARCHAR(160) NOT NULL,
    `price` NUMERIC(5,2) NOT NULL
);

CREATE TABLE `Order`
(
    `id` INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    `timestamp` DATE NOT NULL,
    `metal_id` INTEGER NOT NULL,
    `size_id` INTEGER NOT NULL,
    `style_id` INTEGER NOT NULL,
    FOREIGN KEY(`metal_id`) REFERENCES `Metals`(`id`),
    FOREIGN KEY(`size_id`) REFERENCES `Sizes`(`id`),
    FOREIGN KEY(`style_id`) REFERENCES `Styles`(`id`)
);

INSERT INTO `Metal` VALUES (null, 'Sterling Silver', 12.50);
INSERT INTO `Metal` VALUES (null, '14K Gold', 726.40);
INSERT INTO `Metal` VALUES (null, '24K Gold', 1258.90);
INSERT INTO `Metal` VALUES (null, 'Platinum', 795.45);
INSERT INTO `Metal` VALUES (null, 'Palladium', 1241.00);

INSERT INTO `Size` VALUES (null, 0.5, 405);
INSERT INTO `Size` VALUES (null, 0.75, 782);
INSERT INTO `Size` VALUES (null, 1, 1470);
INSERT INTO `Size` VALUES (null, 1.5, 1997);
INSERT INTO `Size` VALUES (null, 2, 3638);

INSERT INTO `Style` VALUES (null, 'Classic', 500);
INSERT INTO `Style` VALUES (null, 'Modern', 710);
INSERT INTO `Style` VALUES (null, 'Vintage', 965);

INSERT INTO `Order` VALUES (null, '2023-01-01', 3, 2, 3);
INSERT INTO `Order` VALUES (null, '2023-02-02', 4, 5, 2);
INSERT INTO `Order` VALUES (null, '2023-03-03', 1, 1, 1);
INSERT INTO `Order` VALUES (null, '2023-04-04', 5, 4, 3);
INSERT INTO `Order` VALUES (null, '2023-05-05', 2, 3, 2);

SELECT
    o.id,
    o.timestamp,
    o.metal_id,
    o.size_id,
    o.style_id
FROM "Order" o

SELECT
    o.id,
    o.timestamp,
    o.metal_id,
    o.size_id,
    o.style_id
FROM 'Order' o
WHERE o.id = 2

INSERT INTO 'Order'
    ( timestamp, metal_id, size_id, style_id )
VALUES
    ( "2023-07-06", 4, 1, 1);

DELETE FROM 'Order'
WHERE id = 2

UPDATE Metal
SET
    metal = "Sterling Silver",
    price = 15.50
WHERE id = 1

SELECT
    o.timestamp,
    o.size_id,
    o.style_id,
    o.metal_id,
    m.metal metal_name,
    m.price metal_price,
    s.carets size_caret,
    s.price size_price,
    st.style style_name,
    st.price style_price
FROM `Order` o
JOIN Metal m ON m.id = o.metal_id
JOIN Size s ON s.id = o.size_id
JOIN Style st ON st.id = o.style_id