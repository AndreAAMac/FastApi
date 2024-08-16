from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app

# teste segue tres etapas = Arrange, Act, Assert


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Arrange(Organização)

    response = client.get('/')  # Act(Ação)

    assert response.status_code == HTTPStatus.OK  # Assert(Afirmar)
    assert response.json() == {'message': 'Olá Mundo!'}  # Assert
