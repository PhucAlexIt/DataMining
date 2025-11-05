use AdventureWorksLT2022
-- Câu 1: 
select * from SalesLT.Product
select FirstName, LastName from SalesLT.Customer
-- Câu 2:
select top 15 * from SalesLT.ProductModel
select top 20 percent SalesLT.ProductModel.ProductModelID, SalesLT.ProductModel.Name from SalesLT.ProductModel
-- Câu 3:
select max(ListPrice) as 'Max_Price' from SalesLT.Product
select min(ModifiedDate) from SalesLT.Customer