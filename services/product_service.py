from app.database.connection import get_connection

def create_product(data):
    conn = get_connection()
    cur = conn.cursor()

    query = """
    INSERT INTO product(name, price, quantity)
    VALUES (%s, %s, %s)
    RETURNING *
    """

    cur.execute(query, (data.name, data.price, data.quantity))

    product = cur.fetchone()

    conn.commit()

    cur.close()
    conn.close()

    return product

def get_all_products():
    conn = get_connection()
    cur = conn.cursor()

    query = "SELECT * FROM product"

    cur.execute(query)

    products = cur.fetchall()

    cur.close()
    conn.close()

    return products

def get_product(id):
    conn = get_connection()
    cur = conn.cursor()

    query="""
    SELECT * FROM product
    WHERE id = %s
    """

    cur.execute(query, (id,))

    product = cur.fetchone()

    cur.close()
    conn.close()

    return product

def update_product(id, data):
    conn = get_connection()
    cur = conn.cursor()

    query = """
    UPDATE product
    SET name = %s, price =%s, quantity = %s
    WHERE id = %s
    RETURNING *
    """

    values = (data.name, data.price, data.quantity, id)

    cur.execute(query, values)

    updated_product = cur.fetchone()

    conn.commit()

    cur.close()
    conn.close

    return updated_product

def delete_product(id):
    conn = get_connection()
    cur = conn.cursor()

    query = """
    DELETE FROM product
    WHERE id = %s
    RETURNING *
    """

    cur.execute(query, (id,))

    deleted_prd = cur.fetchone()

    conn.commit()

    cur.close()
    conn.close()

    return deleted_prd

def patch_product(id, data):
    conn = get_connection()
    cur = conn.cursor()

    update_fields = []
    values = []

    if data.name is not None:
        update_fields.append("name = %s")
        values.append(data.name)

    if data.price is not None: 
        update_fields.append("price = %s")
        values.append(data.price)

    if data.quantity is not None: 
        update_fields.append("quantity = %s")
        values.append(data.quantity)

    values.append(id)

    query = f"""
    UPDATE product
    SET {', '.join(update_fields)}
    WHERE id = %s
    RETURNING *
    """

    cur.execute(query, tuple(values))

    updated_product = cur.fetchone()

    conn.commit()

    cur.close()
    conn.close()

    return updated_product
