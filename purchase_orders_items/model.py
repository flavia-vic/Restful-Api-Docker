from db import db

class PurchaseOrdersItemsModel(db.Model):
    __tablename__ = 'purchase_orders_items'

    id = db.Column(db.Integer, primary_key=True)  # Identificador único
    description = db.Column(db.String(500), nullable=False)  # Descrição do item
    price = db.Column(db.Numeric(precision=10, scale=2), nullable=False)  # Alterado para db.Numeric para precisão exata em valores monetários
    quantity = db.Column(db.Integer, nullable=False, default=1)  # Adicionado valor padrão
    purchase_order_id = db.Column(db.Integer, db.ForeignKey(
        'purchase_order.id', ondelete="CASCADE"), nullable=False)  # Adicionado ondelete para deletar filhos ao excluir o pai

    def __init__(self, description, price, purchase_order_id, quantity=1):
        self.description = description
        self.price = price
        self.purchase_order_id = purchase_order_id
        self.quantity = quantity

    def as_dict(self):
        """
        Retorna a representação do objeto como um dicionário.
        """
        return {
            'id': self.id,
            'description': self.description,
            'price': float(self.price),  # Convertendo para float para garantir compatibilidade ao serializar
            'quantity': self.quantity,
            'purchase_order_id': self.purchase_order_id
        }

    @classmethod
    def find_by_purchase_order_id(cls, purchase_order_id):
        """
        Encontra itens por ID de ordem de compra.
        """
        return cls.query.filter_by(purchase_order_id=purchase_order_id).all()

    def save(self):
        """
        Salva o item na base de dados.
        """
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e  # Melhor prática para capturar e depurar erros

