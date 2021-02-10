from shorturl import db


class Reg(db.Model):
    slug = db.Column(db.String(1000), primary_key=True)
    website = db.Column(db.String(1000), nullable=False)

    def __init__(self, slug, website):
        self.slug = slug
        self.website = website

