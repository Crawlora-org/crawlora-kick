require "json"
require "net/http"
require "uri"

module Crawlora
  module Kick
    module Errors
      class Error < StandardError
        attr_reader :status, :operation_id, :body

        def initialize(message, status: nil, operation_id: nil, body: nil)
          super(message)
          @status, @operation_id, @body = status, operation_id, body
        end
      end
      class ClientError < Error; end
      class ServerError < Error; end
      class NetworkError < Error; end
    end

    OPERATIONS = JSON.parse(<<~'JSON').freeze
      {"kick-categories": {"bodyParam": null, "bodyRequired": false, "id": "kick-categories", "method": "GET", "params": [], "path": "/kick/categories", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "kick-category-clips": {"bodyParam": null, "bodyRequired": false, "id": "kick-category-clips", "method": "GET", "params": [{"description": "Category slug from kick-subcategories or kick-search-categories, lowercase; a kick.com/category URL is also accepted", "in": "query", "name": "slug", "required": true, "type": "string", "x-example": "just-chatting"}, {"description": "Previous response's next_cursor; omit for the newest page", "in": "query", "name": "cursor", "type": "string", "x-example": "clip_01M5TR7FRZPCDA6BS1NP7HKV4T"}], "path": "/kick/category-clips", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "slug", "required": true, "type": "string"}, {"in": "query", "name": "cursor", "type": "string"}], "security": ["ApiKeyAuth"]}, "kick-channel": {"bodyParam": null, "bodyRequired": false, "id": "kick-channel", "method": "GET", "params": [{"description": "Channel slug from kick.com/{slug}, case-insensitive; a kick.com URL is also accepted", "in": "query", "name": "slug", "required": true, "type": "string", "x-example": "xqc"}], "path": "/kick/channel", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "slug", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "kick-channel-chatroom": {"bodyParam": null, "bodyRequired": false, "id": "kick-channel-chatroom", "method": "GET", "params": [{"description": "Channel slug from kick.com/{slug}, case-insensitive; a kick.com URL is also accepted", "in": "query", "name": "slug", "required": true, "type": "string", "x-example": "xqc"}], "path": "/kick/channel-chatroom", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "slug", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "kick-channel-clips": {"bodyParam": null, "bodyRequired": false, "id": "kick-channel-clips", "method": "GET", "params": [{"description": "Channel slug from kick.com/{slug}, case-insensitive; a kick.com URL is also accepted", "in": "query", "name": "slug", "required": true, "type": "string", "x-example": "xqc"}, {"description": "Previous response's next_cursor; omit for the newest page", "in": "query", "name": "cursor", "type": "string", "x-example": "abc"}], "path": "/kick/channel-clips", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "slug", "required": true, "type": "string"}, {"in": "query", "name": "cursor", "type": "string"}], "security": ["ApiKeyAuth"]}, "kick-channel-emotes": {"bodyParam": null, "bodyRequired": false, "id": "kick-channel-emotes", "method": "GET", "params": [{"description": "Channel slug from kick.com/{slug}, case-insensitive; a kick.com URL is also accepted", "in": "query", "name": "slug", "required": true, "type": "string", "x-example": "xqc"}], "path": "/kick/channel-emotes", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "slug", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "kick-channel-links": {"bodyParam": null, "bodyRequired": false, "id": "kick-channel-links", "method": "GET", "params": [{"description": "Channel slug from kick.com/{slug}, case-insensitive; a kick.com URL is also accepted", "in": "query", "name": "slug", "required": true, "type": "string", "x-example": "xqc"}], "path": "/kick/channel-links", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "slug", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "kick-channel-streams": {"bodyParam": null, "bodyRequired": false, "id": "kick-channel-streams", "method": "GET", "params": [{"description": "Channel slug from kick.com/{slug}, case-insensitive; a kick.com URL is also accepted", "in": "query", "name": "slug", "required": true, "type": "string", "x-example": "xqc"}], "path": "/kick/channel-streams", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "slug", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "kick-channel-videos": {"bodyParam": null, "bodyRequired": false, "id": "kick-channel-videos", "method": "GET", "params": [{"description": "Channel slug from kick.com/{slug}, case-insensitive; a kick.com URL is also accepted", "in": "query", "name": "slug", "required": true, "type": "string", "x-example": "xqc"}], "path": "/kick/channel-videos", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "slug", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "kick-clip": {"bodyParam": null, "bodyRequired": false, "id": "kick-clip", "method": "GET", "params": [{"description": "Clip id from kick-clips' or kick-channel-clips' own clips[].id field", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "clip_01M5SKVA6GGAAAT5YPJ7J43WE4"}], "path": "/kick/clip", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "kick-clips": {"bodyParam": null, "bodyRequired": false, "id": "kick-clips", "method": "GET", "params": [{"description": "Ordering: date is newest first (default), views ranks by views inside the time window", "enum": ["date", "views"], "in": "query", "name": "sort", "type": "string", "x-example": "views"}, {"description": "Window that views ranks within; omit for Kick's default window", "enum": ["day", "week", "month", "all"], "in": "query", "name": "time", "type": "string", "x-example": "week"}, {"description": "Previous response's next_cursor; omit for the first page", "in": "query", "name": "cursor", "type": "string", "x-example": "abc"}], "path": "/kick/clips", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["date", "views"], "in": "query", "name": "sort", "type": "string"}, {"enum": ["day", "week", "month", "all"], "in": "query", "name": "time", "type": "string"}, {"in": "query", "name": "cursor", "type": "string"}], "security": ["ApiKeyAuth"]}, "kick-drops": {"bodyParam": null, "bodyRequired": false, "id": "kick-drops", "method": "GET", "params": [{"description": "Which campaigns to return: active (default), expired or all", "enum": ["active", "expired", "all"], "in": "query", "name": "status", "type": "string", "x-example": "active"}], "path": "/kick/drops", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["active", "expired", "all"], "in": "query", "name": "status", "type": "string"}], "security": ["ApiKeyAuth"]}, "kick-gifts": {"bodyParam": null, "bodyRequired": false, "id": "kick-gifts", "method": "GET", "params": [], "path": "/kick/gifts", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "kick-languages": {"bodyParam": null, "bodyRequired": false, "id": "kick-languages", "method": "GET", "params": [], "path": "/kick/languages", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "kick-livestreams": {"bodyParam": null, "bodyRequired": false, "id": "kick-livestreams", "method": "GET", "params": [{"description": "Ordering: viewer_count_desc is most viewers first (default), featured is Kick's featured order", "enum": ["viewer_count_desc", "featured"], "in": "query", "name": "sort", "type": "string", "x-example": "viewer_count_desc"}, {"description": "Stream language code such as en, ja, es, pt-BR, optionally with a region (2 to 3 letters, then an optional 2 to 4 letter region); see kick-languages for the codes Kick lists", "in": "query", "name": "language", "type": "string", "x-example": "ja"}, {"description": "Category id from kick-subcategories' or kick-search-categories' own id field", "in": "query", "name": "category_id", "type": "integer", "x-example": 15}, {"description": "Page size, 1 to 100; defaults to 24", "in": "query", "name": "limit", "type": "integer", "x-example": 24}, {"description": "Previous response's next_cursor; omit for the first page", "in": "query", "name": "after", "type": "string", "x-example": "eyJvIjoxfQ"}], "path": "/kick/livestreams", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["viewer_count_desc", "featured"], "in": "query", "name": "sort", "type": "string"}, {"in": "query", "name": "language", "type": "string"}, {"in": "query", "name": "category_id", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}, {"in": "query", "name": "after", "type": "string"}], "security": ["ApiKeyAuth"]}, "kick-search-categories": {"bodyParam": null, "bodyRequired": false, "id": "kick-search-categories", "method": "GET", "params": [{"description": "Category name to search for, up to 100 characters", "in": "query", "name": "query", "required": true, "type": "string", "x-example": "chat"}, {"description": "Maximum results, 1 to 100; defaults to 10", "in": "query", "name": "limit", "type": "integer", "x-example": 10}], "path": "/kick/search-categories", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "query", "required": true, "type": "string"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "kick-search-channels": {"bodyParam": null, "bodyRequired": false, "id": "kick-search-channels", "method": "GET", "params": [{"description": "Channel name to search for, up to 100 characters", "in": "query", "name": "query", "required": true, "type": "string", "x-example": "xqc"}, {"description": "Only channels live now", "in": "query", "name": "live", "type": "boolean", "x-example": true}, {"description": "Maximum results, 1 to 100; defaults to 10", "in": "query", "name": "limit", "type": "integer", "x-example": 10}], "path": "/kick/search-channels", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "query", "required": true, "type": "string"}, {"in": "query", "name": "live", "type": "boolean"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "kick-subcategories": {"bodyParam": null, "bodyRequired": false, "id": "kick-subcategories", "method": "GET", "params": [{"description": "Top-level category slug from kick-categories; a parent Kick adds later is also accepted once it appears there", "enum": ["games", "irl", "music", "gambling", "creative", "alternative", "chat-roulette"], "in": "query", "name": "category", "type": "string", "x-example": "irl"}, {"description": "Page number, 1 to 20; defaults to 1", "in": "query", "name": "page", "type": "integer", "x-example": 1}, {"description": "Page size, 1 to 32; defaults to 24", "in": "query", "name": "limit", "type": "integer", "x-example": 10}], "path": "/kick/subcategories", "pathParams": [], "produces": ["application/json"], "queryParams": [{"enum": ["games", "irl", "music", "gambling", "creative", "alternative", "chat-roulette"], "in": "query", "name": "category", "type": "string"}, {"in": "query", "name": "page", "type": "integer"}, {"in": "query", "name": "limit", "type": "integer"}], "security": ["ApiKeyAuth"]}, "kick-subcategory": {"bodyParam": null, "bodyRequired": false, "id": "kick-subcategory", "method": "GET", "params": [{"description": "Category slug from kick-subcategories' or kick-search-categories' own slug field", "in": "query", "name": "slug", "required": true, "type": "string", "x-example": "just-chatting"}], "path": "/kick/subcategory", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "slug", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}, "kick-top-channels": {"bodyParam": null, "bodyRequired": false, "id": "kick-top-channels", "method": "GET", "params": [], "path": "/kick/top-channels", "pathParams": [], "produces": ["application/json"], "queryParams": [], "security": ["ApiKeyAuth"]}, "kick-video": {"bodyParam": null, "bodyRequired": false, "id": "kick-video", "method": "GET", "params": [{"description": "Video uuid (36 characters) from kick-channel-videos or kick-channel-streams, or a kick.com video URL", "in": "query", "name": "id", "required": true, "type": "string", "x-example": "eb707c31-208b-4737-8bcf-a5c9fd187e82"}], "path": "/kick/video", "pathParams": [], "produces": ["application/json"], "queryParams": [{"in": "query", "name": "id", "required": true, "type": "string"}], "security": ["ApiKeyAuth"]}}
    JSON
    OPERATION_IDS = JSON.parse(<<~'JSON').freeze
      ["kick-categories", "kick-category-clips", "kick-channel", "kick-channel-chatroom", "kick-channel-clips", "kick-channel-emotes", "kick-channel-links", "kick-channel-streams", "kick-channel-videos", "kick-clip", "kick-clips", "kick-drops", "kick-gifts", "kick-languages", "kick-livestreams", "kick-search-categories", "kick-search-channels", "kick-subcategories", "kick-subcategory", "kick-top-channels", "kick-video"]
    JSON
    OPERATION_COUNT = OPERATION_IDS.length

    class Client
      attr_reader :base_url

      def initialize(api_key: ENV["CRAWLORA_API_KEY"], base_url: "https://api.crawlora.net/api/v1", timeout: 30, user_agent: "crawlora-kick-ruby/0.1.0", transport: nil)
        @api_key = api_key
        @base_url = base_url.to_s.sub(%r{/+$}, "")
        @timeout = Float(timeout)
        @user_agent = user_agent
        @transport = transport
        @closed = false
      end

      def request(operation_id, params = {}, response_type: :auto)
        raise Errors::ClientError, "client is closed" if @closed
        operation_id = operation_id.to_s
        operation = OPERATIONS[operation_id]
        raise Errors::ClientError.new("unknown operation: #{operation_id}", operation_id: operation_id) unless operation
        raise Errors::ClientError.new("Crawlora API key is required", operation_id: operation_id) if @api_key.nil? || @api_key.to_s.empty?
        normalized = params.each_with_object({}) { |(key, value), out| out[key.to_s] = value }
        payload = request_body(operation, normalized)
        url = build_url(operation, normalized)
        uri = URI.parse(url)
        request = operation["method"] == "POST" ? Net::HTTP::Post.new(uri) : Net::HTTP::Get.new(uri)
        unless payload.nil?
          request.body = payload
          request["Content-Type"] = "application/json"
        end
        request["x-api-key"] = @api_key
        request["User-Agent"] = @user_agent
        request["Accept"] = operation["produces"].include?("text/plain") ? "application/json, text/plain" : "application/json"
        begin
          if @transport
            response = if operation["method"] == "POST"
              @transport.call(url, request.to_hash, @timeout, "POST", payload)
            else
              @transport.call(url, request.to_hash, @timeout)
            end
            status = Integer(response.fetch(:status) { response.fetch("status") })
            body = response.fetch(:body) { response.fetch("body", "") }
            headers = response.fetch(:headers) { response.fetch("headers", {}) }
            content_type = headers["content-type"] || headers["Content-Type"]
          else
            http = Net::HTTP.new(uri.host, uri.port)
            http.use_ssl = uri.scheme == "https"
            http.open_timeout = @timeout
            http.read_timeout = @timeout
            response = http.start { |connection| connection.request(request) }
            status = response.code.to_i
            body = response.body
            content_type = response["content-type"]
          end
        rescue Timeout::Error, SocketError, SystemCallError, IOError, EOFError, Net::HTTPBadResponse, Net::ProtocolError, OpenSSL::SSL::SSLError => error
          raise Errors::NetworkError.new("Crawlora request failed: #{error.message}", operation_id: operation_id)
        end
        unless status >= 200 && status < 300
          klass = status >= 500 ? Errors::ServerError : Errors::ClientError
          raise klass.new("Crawlora returned HTTP #{status}", status: status, operation_id: operation_id, body: body)
        end
        parse_response(body, content_type, operation, normalized, response_type)
      end

      def close
        @closed = true
      end

      def closed?
        @closed
      end

      def with
        return self unless block_given?
        yield self
      ensure
        close if block_given?
      end

      def self.operation_count
        OPERATION_COUNT
      end

      def self.operation_ids
        OPERATION_IDS
      end

      def self.operations
        OPERATIONS
      end

            define_method('categories') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('kick-categories', params, response_type: response_type)
      end
      define_method('category_clips') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('kick-category-clips', params, response_type: response_type)
      end
      define_method('channel') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('kick-channel', params, response_type: response_type)
      end
      define_method('channel_chatroom') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('kick-channel-chatroom', params, response_type: response_type)
      end
      define_method('channel_clips') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('kick-channel-clips', params, response_type: response_type)
      end
      define_method('channel_emotes') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('kick-channel-emotes', params, response_type: response_type)
      end
      define_method('channel_links') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('kick-channel-links', params, response_type: response_type)
      end
      define_method('channel_streams') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('kick-channel-streams', params, response_type: response_type)
      end
      define_method('channel_videos') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('kick-channel-videos', params, response_type: response_type)
      end
      define_method('clip') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('kick-clip', params, response_type: response_type)
      end
      define_method('clips') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('kick-clips', params, response_type: response_type)
      end
      define_method('drops') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('kick-drops', params, response_type: response_type)
      end
      define_method('gifts') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('kick-gifts', params, response_type: response_type)
      end
      define_method('languages') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('kick-languages', params, response_type: response_type)
      end
      define_method('livestreams') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('kick-livestreams', params, response_type: response_type)
      end
      define_method('search_categories') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('kick-search-categories', params, response_type: response_type)
      end
      define_method('search_channels') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('kick-search-channels', params, response_type: response_type)
      end
      define_method('subcategories') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('kick-subcategories', params, response_type: response_type)
      end
      define_method('subcategory') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('kick-subcategory', params, response_type: response_type)
      end
      define_method('top_channels') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('kick-top-channels', params, response_type: response_type)
      end
      define_method('video') do |**params|
        response_type = params.delete(:response_type) || params.delete(:_response_type) || :auto
        request('kick-video', params, response_type: response_type)
      end

      private

      # POST operations take their JSON body under the body parameter name or "body".
      def request_body(operation, params)
        name = operation["bodyParam"]
        return nil if name.nil?
        value = params.key?(name) ? params[name] : params["body"]
        if value.nil?
          raise Errors::ClientError.new("missing request body: #{name}", operation_id: operation["id"]) if operation["bodyRequired"]
          return nil
        end
        value.is_a?(String) ? value : JSON.generate(value)
      end

      def build_url(operation, params)
        known = operation["params"].map { |param| param["name"] }
        known << "body" if operation["bodyParam"]
        unknown = params.keys - known
        raise Errors::ClientError.new("unknown parameters: #{unknown.join(', ')}", operation_id: operation["id"]) unless unknown.empty?
        path = operation["path"].dup
        operation["params"].select { |param| param["in"] == "path" }.each do |param|
          value = params[param["name"]]
          raise Errors::ClientError.new("missing path parameter: #{param['name']}", operation_id: operation["id"]) if value.nil?
          path.sub!("{" + param["name"] + "}", percent_encode(value.to_s))
        end
        pairs = []
        operation["queryParams"].each do |param|
          name = param["name"]
          value = params.key?(name) ? params[name] : param["default"]
          if value.nil?
            raise Errors::ClientError.new("missing query parameter: #{name}", operation_id: operation["id"]) if param["required"]
            next
          end
          enum_values = param["enum"] || (param["items"] && param["items"]["enum"])
          if enum_values && !(value.is_a?(Array) ? value : [value]).all? { |item| enum_values.map(&:to_s).include?(item.to_s) }
            raise Errors::ClientError.new("invalid value for #{name}", operation_id: operation["id"])
          end
          if value.is_a?(Array)
            format = param["collectionFormat"] || "csv"
            if format == "multi"
              value.each { |item| pairs << [name, scalar(item)] }
            else
              separator = {"csv" => ",", "ssv" => " ", "tsv" => "\t", "pipes" => "|"}[format] || ","
              pairs << [name, value.map { |item| scalar(item) }.join(separator)]
            end
          else
            pairs << [name, scalar(value)]
          end
        end
        query = pairs.map { |name, value| "#{percent_encode(name)}=#{percent_encode(value)}" }.join("&")
        @base_url + path + (query.empty? ? "" : "?" + query)
      end

      def scalar(value)
        value == true ? "true" : (value == false ? "false" : value.to_s)
      end

      def percent_encode(value)
        URI::DEFAULT_PARSER.escape(value.to_s, /[^A-Za-z0-9\-._~]/)
      end

      def parse_response(body, content_type, operation, params, response_type)
        type = response_type.to_s
        raise Errors::ClientError.new("response_type must be auto, json, or text", operation_id: operation["id"]) unless %w[auto json text].include?(type)
        format = operation["params"].find { |param| param["name"] == "format" }
        text_formats = format && format["enum"] ? format["enum"].reject { |value| %w[json application/json].include?(value.to_s.downcase) } : []
        raw_format = params["format"] && text_formats.include?(params["format"].to_s)
        json_format = format && format["enum"] && format["enum"].any? { |value| %w[json application/json].include?(value.to_s.downcase) } && %w[json application/json].include?(params["format"].to_s.downcase)
        is_json = json_format || content_type.to_s.downcase.include?("json") || operation["produces"] == ["application/json"]
        return body if type == "text" || raw_format || (type == "auto" && !is_json)
        JSON.parse(body)
      rescue JSON::ParserError => error
        raise Errors::Error.new("invalid JSON response from Crawlora: #{error.message}", operation_id: operation["id"], body: body)
      end

      public
    end
  end
end
