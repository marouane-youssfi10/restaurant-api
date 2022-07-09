# @pytest.mark.django_db
# def test_category_retrieve(api_client, user):
#     customer = CustomerFactory(user=user)
#     url = reverse(
#         "customers:profiles-detail",
#         args=[
#             customer.pkid,
#         ],
#     )
#     assert url == f"/api/profiles/{customer.pkid}/"
#     api_client.force_authenticate(user)
#     response = api_client.get(url)
#     assert response.status_code == status.HTTP_200_OK, response.content
#     assert response.json()["customers"]["full_name"] ==
#    customer.user.get_full_name
#     assert response.json()["customers"]["gender"] == customer.gender
#     assert response.json()["customers"]["city"] == customer.city
#     assert response.json()["customers"]["user_info"]["email"] == customer.user.email
