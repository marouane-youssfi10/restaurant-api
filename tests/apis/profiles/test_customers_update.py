# @pytest.mark.django_db
# def test_address_update(api_client, user, food):
#     customer = CustomerFactory(user=user, phone_number="21264126212")
#     url = reverse(
#         "customers:profiles-detail",
#         args=[
#             customer.pkid,
#         ],
#     )
#     assert url == f"/api/profiles/{customer.pkid}/"
#     api_client.force_authenticate(user)
#     response = api_client.patch(
#         url,
#         data={
#             "city": "meknes",
#         },
#     )
#     assert response.status_code == status.HTTP_200_OK, response.content
#     assert response.json()["customers"]["city"] == "meknes"
#     customer.refresh_from_db()
#     assert customer.city == response.json()["customers"]["city"]
# response = api_client.put(
#     url,
#     data={
#         "gender": "female",
#         "phone_number": "+21262612744",
#         "address": "street 1 updated ",
#         "country": "fes",
#         "city": "meknes updated"
#     }
# )
# assert response.status_code == status.HTTP_200_OK, response.content
