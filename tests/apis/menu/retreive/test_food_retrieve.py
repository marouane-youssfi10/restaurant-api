# @pytest.mark.django_db
# def test_food_retrieve(api_client, user, food):
#     url = reverse(
#         "menu:foods-detail",
#         args=[
#             food.pkid,
#         ],
#     )
#     assert url == f"/api/menu/foods/{food.pkid}/"
#     api_client.force_authenticate(user)
#     response = api_client.get(url)
#     assert response.status_code == status.HTTP_200_OK, response.content
#     assert response.json()["food_name"] == food.food_name
#     assert response.json()["slug"] == food.slug
#     assert response.json()["description"] == food.description
#     assert response.json()["price"] == food.price
#     assert (
#         response.json()["category_info"]["category_name"] ==
#        food.category.category_name
#     )
