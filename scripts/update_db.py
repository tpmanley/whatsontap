from whatsontap import db, Tap, app


with app.app_context():
    session = db.session()
    db.metadata.create_all(db.engine)
    session.merge(Tap(id=1,
                    name="Short Circuit Stout",
                    style="sweet stout",
                    abv="5.4%",
                    description="""Short Circuit Stout is a full-bodied and roasty stout with a lingering sweet aftertaste.
It uses 5 different malts to create a variety of flavors that change through the course of taking a sip.""",
                    image="http://placekitten.com/200/200"))
    session.merge(Tap(id=2,
                    name="Flip Switch IPA",
                    style="American IPA",
                    abv="6.1%",
                    description="""Flip Switch IPA is a hoppy American pale ale with a slight citrus aroma. It features
a variety of American hops, with just the right amount of bitterness to match the malty base.""",
                    image="http://placekitten.com/200/200"))
    session.commit()