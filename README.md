# Vehicle Insurance Management (Odoo 18)

## **Overview**

This is a demo app module named **Vehicle Insurance Management** module for Odoo 18 helps businesses manage **insurance policies, claims, and customers** efficiently. It includes:

- **Customer Management**
- **Insurance Policy Handling**
- **Claim Processing**
- **Status Tracking for Policies & Claims**
- **Dropdown Selection for Status & Policy Types**
- **Manage all necesarry schedule in digital calender**
- **a module for storing all employee information**

## **Features**

- Manage **Customers** with associated policies.
- Assign an **Insurance Policy Type** automatically.
- Policies update the **Customer's existing policy type & status**.
- Submit and track **Claims**, with **Claim Purpose selection**.
- **Dropdown-based Status updates** for policies and claims.
- **Kanban View** for Policies with a clean UI.

---

## **Installation Steps**

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/mahmudaakterdisa/odoo-vehicle-insurance-management.git
cd odoo-vehicle-insurance-management
```

### **2️⃣ Move Module to Odoo Addons Directory**

Move the module folder(`/vehicle_insurance`) to Odoo's `custom addons` directory(`../custom_addons/`):

```bash
mv vehicle_insurance /path/to/odoo/custom_addons/
```

copy `odoo.conf` configuration file to odoo's root directory (`../odoo-18.0/`)

### **3️⃣ Install Dependencies**

Ensure you have all dependencies installed.

run following command from the root directory of odoo:

```bash
pip install -r requirements.txt
```

### **4️⃣ Create Database in PostgreSQL server and run it**
create an user `odoo` and create database by following command in any sql tool or in pycharm terminal:
```bash
CREATE DATABASE vehicle_insurance OWNER odoo ENCODING 'UTF8' TEMPLATE template1;
```

then, run following command to run the server from command line:
```bash
python odoo-bin -c odoo.conf -d odoo_insurance -u vehicle_insurance
```

### **5️⃣ Login to Odoo & Install the Module**

- Open your browser and go to `http://localhost:8069`
- Login as **admin** with password **admin**
- Go to **Apps** → Search for `Vehicle Insurance Management`
- Click **Install**

---

## **How to Use**

### **1️⃣ Manage Customers**

- Navigate to **Insurance > Customers**
- Add new customers & their details.
- The **Existing Insurance Policy Type** will update automatically when a policy is assigned.

### **2️⃣ Create & Manage Policies**

- Navigate to **Insurance > Policies**
- Create new insurance policies.
- **Policy Status updates automatically in Customer Records**.

### **3️⃣ Submit & Track Claims**

- Navigate to **Insurance > Claims**
- Choose **Claim Purpose** (Damage, Accident, etc.)
- **Status is manually selectable** from the dropdown.

### **4️⃣ View Policies in Kanban View**

- Click on **Kanban View** in the **Policies** menu.
- Policies display in an organized card layout.


