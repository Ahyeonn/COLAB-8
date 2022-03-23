<script>
import BaseInput from "@/components/Form/BaseInput";
import BaseButton from "@/components/UI/BaseButton";
import BaseModal from "@/components/BaseModal";

import {mapGetters} from 'vuex'
import useVuelidate from '@vuelidate/core'
import {required, alpha, minLength, integer} from '@vuelidate/validators'

export default {
  name: "ContactInfo",
  components: {
    BaseInput,
    BaseButton,
    BaseModal
  },
  setup: () => ({v$: useVuelidate()}),
  data() {
    return {
      isVisible: false,
      contact: {
        name: '',
        phoneNumber: ''
      }
    }
  },
  validations() {
    return {
      contact: {
        name: {
          required,
          alpha,
          minLength: minLength(3),
          $autoDirty: true,
        },
        phoneNumber: {
          required,
          integer,
          minLength: minLength(10),
          $autoDirty: true,
        }
      }
    }
  },
  computed: {
    ...mapGetters(['getContacts'])
  },
  methods: {
    toggleModal() {
      this.isVisible = !this.isVisible;
    },
    addContact() {
      this.$store.commit('ADD_CONTACT', this.contact)
      this.contact = {}
      this.isVisible = false
    },
  }
}

</script>

<template>
  <h2 class="my-4 text-md-center">📞 Almost there! Just enter everyone’s contact details! </h2>
  <div class="row">
    <div class="col-md-6 mx-auto">
      <div class="card shadow">
        <div class="card-body">
          <form @submit.prevent>
            <!-- Host phone-number -->
            <div class="mb-3">
              <BaseInput
                  class="form-control"
                  name="host-phone-number"
                  label="Your number"
                  type="tel"
              />
            </div>

            <!-- contact list -->
            <ul class="list-unstyled contacts">
              <li v-for="(contacts, index) in getContacts" :key="index">
                <svg class="rounded-circle p-2 me-3 my-3" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"
                     width="24" height="24">
                  <path fill="none" d="M0 0h24v24H0z" />
                  <path d="M20 22H4v-2a5 5 0 0 1 5-5h6a5 5 0 0 1 5 5v2zm-8-9a6 6 0 1 1 0-12 6 6 0 0 1 0 12z" />
                </svg>
                <span>{{ contacts }}</span>
              </li>
            </ul>

            <button
                class="btn add-contact px-0 d-flex align-items-center mx-auto"
                type="button"
                @click="toggleModal"
                data-bs-toggle="modal"
                data-bs-target="#addContact"
            >
              <svg class="rounded-circle plus me-3" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24"
                   height="24">
                <path fill="none" d="M0 0h24v24H0z" />
                <path d="M11 11V5h2v6h6v2h-6v6h-2v-6H5v-2z" />
              </svg>
              Add more contacts
            </button>

            <!-- Modal -->
            <base-modal @close="toggleModal" :modalActive="isVisible">
              <h4 class="text-center text-primary mb-3">Add Contact</h4>
              <!-- Contact name -->
              <div class="mb-3">
                <BaseInput class="form-control"
                           name="contact-name"
                           label="Name"
                           required
                           :modelValue="contact.name"
                           @input="(event) => contact.name = event.target.value"
                           :invalid="v$.contact.name.$error"
                />
                <!-- Display errors -->
                <template v-if="v$.contact.name.$error">
                  <template
                      v-for="(error, index) of v$.contact.name.$errors"
                      :key="index"
                  >
                    <p>{{ error.$message }}</p>
                  </template>
                </template>
              </div>

              <!-- Contact Phone number -->
              <div class="mb-3">
                <BaseInput class="form-control"
                           name="contact-phone-number"
                           label="Phone number"
                           required
                           :modelValue="contact.phoneNumber"
                           @input="(event) => contact.phoneNumber = event.target.value"
                           :invalid="v$.contact.phoneNumber.$error"
                />
                <!-- Display errors -->
                <template v-if="v$.contact.phoneNumber.$error">
                  <template
                      v-for="(error, index) of v$.contact.phoneNumber.$errors"
                      :key="index"
                  >
                    <p>{{ error.$message }}</p>
                  </template>
                </template>
              </div>


              <div class="text-center">
                <BaseButton type="button" class="btn-primary mt-4 py-2 w-75 text-white shadow-sm text-center"
                            label="Add"
                            @click="addContact"
                />
              </div>
            </base-modal>


            <div class="text-center">
              <BaseButton
                  class="btn-primary mt-4 py-2 w-75 text-white shadow-sm"
                  type="submit"
                  label="Continue"
              />
              <router-link
                  class="btn btn-back mt-3 py-2 w-75 mx-auto d-block shadow-sm"
                  to="/"
              >Go back
              </router-link>

            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped lang="scss">
.contacts {
  svg {
    border : 1px solid gray;
    width  : 40px;
    height : 40px;
    }
  }

.add-contact {
  width  : 100%;
  color  : $green;
  border : none;

  .plus {
    width      : 40px;
    height     : 40px;
    padding    : 5px;
    background : #E3F6EB;
    fill       : $green;
    }
  }
</style>
