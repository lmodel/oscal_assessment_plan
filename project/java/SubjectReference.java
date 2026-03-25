package None;

/* metamodel_version: 1.7.0 */
import java.util.List;
import lombok.*;

/**
  A human-oriented identifier reference to a resource. Use type to indicate whether the identified resource is a component, inventory item, location, user, or something else.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class SubjectReference  {

  private String subject-uuid;
  private String type;
  private String title;
  private String remarks;
  private List<Property> props;
  private List<Link> links;

}