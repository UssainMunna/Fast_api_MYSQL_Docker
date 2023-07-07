from fastapi import FastAPI, Request
from pydantic import BaseModel
import mysql.connector

app = FastAPI()

class Item(BaseModel):
    security_code: str
    security_name: str
    client_name: str
    deal_type:str
    quantity:str
    price:str

@app.get('/get_users')
async def root():
    print("checking database")
    get_all_user = []
    data_base_ = mysql.connector.connect(
    user='root', password='root', host='mysql', port="3306", database='bse_table')
    cursor = data_base_.cursor()
    cursor.execute("SELECT * FROM bse_table.bse_info")
    myresult = cursor.fetchall()
    print(myresult)
    for x in myresult:
       get_all_user.append(x)
    return myresult
 
@app.get('/get_users/{item_id}')
async def root(item_id: int,item: Item):
    print("checking database")
    get_all_user = []
    data_base_ = mysql.connector.connect(
    user='root', password='root', host='mysql', port="3306", database='bse_table')
    cursor = data_base_.cursor()
    cursor.execute(f"SELECT * FROM bse_table.bse_info where id ={item_id};")
    myresult = cursor.fetchall()
    print(myresult)
    for x in myresult:
       get_all_user.append(x)
    return myresult
 

@app.post("/create_user")
async def create_item(item: Item):
   try:
      security_code = item.security_code
      security_name = item.security_name
      client_name = item.client_name
      deal_type = item.deal_type
      quantity = item.quantity
      price = item.price
      insert_query = f"INSERT INTO bse_info (security_code,security_name,client_name,deal_type,quantity,price) VALUES ('{security_code}','{security_name}','{client_name}','{deal_type}','{quantity}','{price}');"
      data_base_ = mysql.connector.connect(user='root', password='root', host='mysql', port="3306", database='bse_table')
      cursor = data_base_.cursor()
      cursor.execute(insert_query)
      data_base_.commit()
      cursor.close()
      return {
         "Message": "User Created",
         "id": cursor.lastrowid
      }
   except Exception as e:
      return str(e)
   
@app.put("/update_user/{item_id}")
async def create_item(item_id: int,item: Item):
   try:
      security_code = item.security_code
      security_name = item.security_name
      client_name = item.client_name
      deal_type = item.deal_type
      quantity = item.quantity
      price = item.price
      update_query = f"UPDATE bse_info SET security_code = '{security_code}', security_name = '{security_name}',client_name = '{client_name}', deal_type = '{deal_type}', quantity = '{quantity}',price = '{price}' WHERE id = '{item_id}'"
      data_base_ = mysql.connector.connect(user='root', password='root', host='mysql', port="3306", database='bse_table')
      cursor = data_base_.cursor()
      cursor.execute(update_query)
      data_base_.commit()
      cursor.close()
      return {
         "Message": "User Updated"}
   except Exception as e:
      return str(e)
   

@app.delete('/{item_id}')
async def root(item_id: int,item: Item):
    print("checking database")
    get_all_user = []
    data_base_ = mysql.connector.connect(
    user='root', password='root', host='mysql', port="3306", database='bse_table')
    cursor = data_base_.cursor()
    cursor.execute(f"DELETE FROM bse_info WHERE id = '{item_id}'")
    data_base_.commit()
    cursor.close()
    return {
      "Message": "User Deleted"}
