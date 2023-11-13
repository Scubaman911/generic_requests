
get_user_by_id = """ query ($id: ID!) {
  user(id: $id) {
    id
  }
}"""