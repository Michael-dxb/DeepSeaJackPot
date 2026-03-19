platform :ios do
  desc "Upload IPA to App Store Connect"
  lane :upload do
    api_key = app_store_connect_api_key(
      key_id: ENV["APP_STORE_CONNECT_API_KEY_KEY_ID"],
      issuer_id: ENV["APP_STORE_CONNECT_API_KEY_ISSUER_ID"],
      key_content: ENV["APP_STORE_CONNECT_API_KEY_KEY"],
      duration: 1200,
      in_house: false
    )

    upload_to_app_store(
      ipa: "./app.ipa",
      api_key: api_key,
      skip_metadata: true,
      skip_screenshots: true,
      submit_for_review: false
    )
  end
end