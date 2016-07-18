# encoding: utf-8
# Code generated by Microsoft (R) AutoRest Code Generator 0.17.0.0
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.

module Azure::ARM::Web
  module Models
    #
    # Collection of ceritificate orders
    #
    class CertificateOrderCollection

      include MsRestAzure

      # @return [Array<CertificateOrder>] Collection of resources
      attr_accessor :value

      # @return [String] Link to next page of resources
      attr_accessor :next_link


      #
      # Mapper for CertificateOrderCollection class as Ruby Hash.
      # This will be used for serialization/deserialization.
      #
      def self.mapper()
        {
          required: false,
          serialized_name: 'CertificateOrderCollection',
          type: {
            name: 'Composite',
            class_name: 'CertificateOrderCollection',
            model_properties: {
              value: {
                required: false,
                serialized_name: 'value',
                type: {
                  name: 'Sequence',
                  element: {
                      required: false,
                      serialized_name: 'CertificateOrderElementType',
                      type: {
                        name: 'Composite',
                        class_name: 'CertificateOrder'
                      }
                  }
                }
              },
              next_link: {
                required: false,
                serialized_name: 'nextLink',
                type: {
                  name: 'String'
                }
              }
            }
          }
        }
      end
    end
  end
end