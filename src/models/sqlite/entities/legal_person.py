from sqlalchemy import Column, String, BIGINT

class LegalPersonTable():
    __tablename__ = "legalperson"

    id = Column(BIGINT, primary_key=True)
    monthly_income = Column(BIGINT, nullable=False)
    full_name = Column(String, nullable=False)
    age = Column(BIGINT, nullable=False)
    email = Column(String, nullable=False)
    cellphone_number = Column(String, nullable=False)
    category = Column(String, nullable=False)
    balance = Column(BIGINT, nullable=False)
    cnpj = Column(String, nullable=False)

    def __repr__(self):
        return (
            f"LegalPerson [name={self.full_name},"
            f"monthly_income={self.monthly_income},"
            f"age={self.age},"
            f"email={self.email},"
            f"cellphone_number={self.cellphone_number},"
            f"category={self.category},"
            f"balance={self.balance},"
            f"cnpj={self.cnpj}]"
        )