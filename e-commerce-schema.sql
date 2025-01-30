/**
given the following, create e-commerce database tables for an online store:

- Tables
-- Products
--- ProductID (primary key and sequence auto increment starting with value 1)
--- Name
--- Description
--- Price
--- CategoryID (foreign key to Categories table)
--- ImageURL
-- Categories
--- CategoryID (primary key and sequence number auto increment starting with value 1)
--- Name
-- Customers
--- CustomerID (primary key and sequence number auto increment starting with value 1)
--- FirstName
--- LastName
--- Email
--- Phone
--- Address
-- Orders
--- OrderID (primary key and sequence number auto increment starting with value 1)
--- CustomerID (foreign key to Customers table)
--- OrderDate
--- ShippingAddress
--- BillingAddress
--- TotalAmount
-- OrderItems
--- OrderItemID (primary key and sequence number auto increment starting with value 1)
--- OrderID (foreign key to Orders table)
--- ProductID (foreign key to Products table)
--- Quantity
--- UnitPrice
-- Shipping
--- ShippingID (primary key and sequence number auto increment starting with value 1)
--- OrderID (foreign key to Orders table)
--- Shipper (shipping company name)
--- TrackingNumber
-- Reviews
--- ReviewID (primary key and sequence number auto increment starting with value 1)
--- CustomerID (foreign key to Customers table)



create database my-ecomm;mysql if the tables do not exist for a  database called my-ecomm
*/ 
  create table if not exists products (
    product_id int not null auto_increment primary key,
    name varchar(255) not null,
    description text,
    price decimal(10,2) not null,
    category_id int not null,
    image_url varchar(255),
    constraint fk_products_categories foreign key (category_id) references categories(category_id)
  );

  create table if not exists categories (
    category_id int not null auto_increment primary key,
    name varchar(255) not null
  );

  create table if not exists customers (
    customer_id int not null auto_increment primary key,
    first_name varchar(255) not null,
    last_name varchar(255) not null,
    email varchar(255) not null,
    phone varchar(255),
    address text
  );

  create table if not exists orders (
    order_id int not null auto_increment primary key,
    customer_id int not null,
    order_date datetime not null,
    shipping_address text,
    billing_address text,
    total_amount decimal(10,2) not null,
    constraint fk_orders_customers foreign key (customer_id) references customers(customer_id)
  );

  create table if not exists order_items (
    order_item_id int not null auto_increment primary key,
    order_id int not null,
    product_id int not null,
    quantity int not null,
    unit_price decimal(10,2) not null,
    constraint fk_order_items_orders foreign key (order_id) references orders(order_id),
    constraint fk_order_items_products foreign key (product_id) references products(product_id)
  );

  create table if not exists shipping (
    shipping_id int not null auto_increment primary key,
    order_id int not null,
    shipper varchar(255) not null,
    tracking_number varchar(255),
    constraint fk_shipping_orders foreign key (order_id) references orders(order_id)
  );

  create table if not exists reviews (
    review_id int not null auto_increment primary key,
    customer_id int not null,
    product_id int not null,
    rating int not null,
    comment text,
    constraint fk_reviews_customers foreign key (customer_id) references customers(customer_id),
    constraint fk_reviews_products foreign key (product_id) references products(product_id)
  ); 




/**

-- select all order over $50 given a customer name. Return the product list with order id, product ID, product name, product image, shipper Name and shipper tracking number

-- select all reviews given a product name. Return the customer name, review, rating

-- create a function for GetProductsByCategory

-- create a procedure for GetProductsByCategory

*/

/**
given a json object with a list of items for a  customer
json object will have the following format:

{
    customer_id: 1,
    order_date: '2022-01-01',
    shipping_address: '123 Main St',
    billing_address: '456 Main St',
    tracking_number: 'ABC123',
    shipper: 'FedEx',
    total_amount: 300,
    items: [
        {
            product_id: 1,
            quantity: 2,
            unit_price: 100

        },
        {
            product_id: 2,
            quantity: 1,
            unit_price: 200
        }
    ]
}

Given the above json object
And the customer exists in the customers table
Then add the order to the orders table and use the returned orderId for insert into other tables
And add a record to the ORDERITEMS table for each order item in the json
And add the shipping record to the shipping table

do not add the customer to the customer table
call the procedure AddOrders2
*/
 delimiter //
 create procedure if not exists AddOrders2(json_data json) 
  begin
    declare customer_id int;
    declare order_id int;
    declare order_date datetime;
    declare shipping_address text;
    declare billing_address text;
    declare tracking_number varchar(255);
    declare shipper varchar(255);
    declare total_amount decimal(10, 2);
    declare items json;
    declare item json;
    declare product_id int;
    declare quantity int;
    declare unit_price decimal(10, 2);

    set customer_id = json_unquote(json_extract(json_data, '$.customer_id'));
    set order_date = json_unquote(json_extract(json_data, '$.order_date'));
    set shipping_address = json_unquote(json_extract(json_data, '$.shipping_address'));
    set billing_address = json_unquote(json_extract(json_data, '$.billing_address'));
    set tracking_number = json_unquote(json_extract(json_data, '$.tracking_number'));
    set shipper = json_unquote(json_extract(json_data, '$.shipper'));
    set total_amount = json_unquote(json_extract(json_data, '$.total_amount'));
    set items = json_extract(json_data, '$.items');

    insert into orders (customer_id, order_date, shipping_address, billing_address, total_amount)     values (customer_id, order_date, shipping_address, billing_address, total_amount);

    set order_id = last_insert_id();

    insert into shipping (order_id, shipper, tracking_number)     values (order_id, shipper, tracking_number);

    while (json_length(items) > 0) do
      set item = json_extract(items, '$[0]');
      set product_id = json_unquote(json_extract(item, '$.product_id'));
      set quantity = json_unquote(json_extract(item, '$.quantity'));
      set unit_price = json_unquote(json_extract(item, '$.unit_price'));

      insert into order_items (order_id, product_id, quantity, unit_price)       values (order_id, product_id, quantity, unit_price);

      set items = json_remove(items, '$[0]');
    end while; 
  end //
  delimiter ;   