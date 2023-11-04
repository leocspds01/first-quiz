import pets_db as pets_db
from question4 import sql_pets_older_than_owner,sql_pets_owned_by_nobody,sql_only_owned_by_bessie 

def test_question4_pets_older_than_owner():
  pets_db.create_db()

  with pets_db.get_connection() as con:
    res = con.execute('''
        SELECT COUNT(*) AS count
        FROM animals A
        JOIN people_animals PA ON A.animal_id = PA.pet_id
        JOIN people P ON PA.owner_id = P.person_id
        WHERE A.age > P.age
    ''')
    result = res.fetchone()

  assert len(result) == 1
  assert result[0] == 2

def test_question4_pets_owned_by_nobody():
  pets_db.create_db()

  with pets_db.get_connection() as con:
    res = con.execute('''
        SELECT name, species, age 
        FROM animals 
        WHERE animal_id NOT IN (SELECT pet_id FROM people_animals)
    ''')
    rows = res.fetchall()

  rows.sort()

  assert len(rows) == 2
  assert rows[0] == ('petey', 'gray whale', 38)
  assert rows[1] == ('shannon', 'cow', 14)

def test_question4_only_owned_by_bessie():
 pets_db.create_db()

 with pets_db.get_connection() as con:
    res = con.execute('''
        SELECT P.name, A.name, A.species
        FROM animals A
        JOIN people_animals PA ON A.animal_id = PA.pet_id
        JOIN people P ON PA.owner_id = P.person_id
        WHERE P.name = 'bessie'
          AND NOT EXISTS (
            SELECT 1 FROM people_animals PA2
            WHERE PA2.pet_id = A.animal_id AND PA2.owner_id != P.person_id
        )
    ''')
    rows = res.fetchall()

    rows.sort()

    assert len(rows) == 2
    assert rows[0] == ('bessie', 'leyla', 'gray whale')
    assert rows[1] == ('bessie', 'randolph', 'lemur')